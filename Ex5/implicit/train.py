  
def train_model(model, train_loader, val_loader, optimizer, criterion, nepochs=15, eval_every=100, out_dir='output'):
  
  liveloss = PlotLosses()   # to plot training progress
  losses = {'loss': None,
            'val_loss': None}

  best = float('inf')
  it = 0 # iteration counter
  for epoch in range(nepochs):

    losses['loss'] = []       # initialize emtpy container for training losses
    for pts, occ in train_loader:
      it += 1

      # Insert your code here
      # 数据转移到GPU
      if torch.cuda.is_available():
          pts, occ = pts.cuda(), occ.cuda()
          
          
      optimizer.zero_grad()  # 清空梯度
      scores = model(pts)    # 前向传播
      loss = criterion(scores, occ).mean()  # 计算损失
      loss.backward()        # 反向传播
      optimizer.step()       # 更新参数
      losses['loss'].append(loss.item())  # 记录损失值

      if (it == 1) or (it % eval_every == 0): # 首次或者每隔一定步数进行验证
        
        with torch.no_grad():
          val_loss = []
          for val_pts, val_occ in val_loader:
            if torch.cuda.is_available():
              val_pts, val_occ = val_pts.cuda(), val_occ.cuda()
            # optimizer.zero_grad() #验证的过程没有bp，不需要清空梯度
            val_scores = model(val_pts)
            val_loss_i = criterion(val_scores, val_occ).mean()
            # Insert your code here
          
            val_loss.append(val_loss_i)
          val_loss = torch.stack(val_loss).mean().item()
          
          if val_loss < best:     # keep track of best model
            best = val_loss
            torch.save(model.state_dict(), os.path.join(out_dir, 'model_best.pt'))

    # update liveplot with latest values
    losses['val_loss'] = val_loss
    losses['loss'] = np.mean(losses['loss'])     # average over all training losses
    liveloss.update(losses)
    liveloss.send()

train_model(model, train_loader, val_loader, optimizer, criterion, nepochs=25, eval_every=100, out_dir=out_dir)
