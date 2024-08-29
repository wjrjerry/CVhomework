import torch


###########################
#### Exercise Function ####
###########################
class StereoMatchingNetwork(torch.nn.Module):
    def __init__(self):
        """
        Implementation of the network layers.
        Layer output tensor size: (batch_size, n_features, height - 8, width - 8)
        """
        super().__init__()
        gpu = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

        #######################################
        # -------------------------------------
        # TODO: ENTER CODE HERE (EXERCISE 5)
        # -------------------------------------
        self.conv1 = torch.nn.Sequential(
            torch.nn.Conv2d(
                in_channels=1,
                out_channels=64,
                kernel_size=3,
                stride=1,
                padding=0,
            ),
            torch.nn.ReLU()
        )

        self.conv2 = torch.nn.Sequential(
            torch.nn.Conv2d(
                in_channels=64,
                out_channels=64,
                kernel_size=3,
                stride=1,
                padding=0,
            ),
            torch.nn.ReLU()
        )

        self.conv3 = torch.nn.Sequential(
            torch.nn.Conv2d(
                in_channels=64,
                out_channels=64,
                kernel_size=3,
                stride=1,
                padding=0,
            ),
            torch.nn.ReLU()
        )

        self.conv4 = torch.nn.Sequential(
            torch.nn.Conv2d(
                in_channels=64,
                out_channels=64,
                kernel_size=3,
                stride=1,
                padding=0,
            )
        )

        self.layers = torch.nn.Sequential(
            self.conv1,
            self.conv2,
            self.conv3,
            self.conv4
        ).to(gpu)

        # Hint: Don't forget to move the modules to the gpu

    def forward(self, X):
        """
        The forward pass of the network. Returns the features for a given image patch.

        Args:
            X (torch.Tensor): image patch of shape (batch_size, height, width, n_channels)

        Returns:
            features (torch.Tensor): predicted normalized features of the input image patch X,
                               shape (batch_size, height - 8, width - 8, n_features)
        """
        #######################################
        # -------------------------------------
        # TODO: ENTER CODE HERE (EXERCISE 5)
        # -------------------------------------
        X = X.permute(0, 3, 1, 2)
        X = self.layers(X)
        features = torch.nn.functional.normalize(X, dim=1, p=2).permute(0, 2, 3, 1)

        return features
