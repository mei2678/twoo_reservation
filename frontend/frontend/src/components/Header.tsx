import React from 'react';
import { AppBar, Box, Toolbar, IconButton, Menu, MenuItem, useTheme } from '@mui/material';
import AccountCircle from '@mui/icons-material/AccountCircle';
import LogoImage from '../images/twoologo.png';

export const Header = () => {
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const theme = useTheme();

  const handleMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  }

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position='static' elevation={0}>
        <Toolbar>
          <Box sx={{ flexGrow: 1, display: 'flex', alignItems: 'center' }}>
            <img src={LogoImage} alt="logo" style={{ maxHeight: '70px' }}/>
          </Box>
          <IconButton
            size="large"
            aria-label="account of current user"
            aria-controls="menu-appbar"
            aria-haspopup="true"
            onClick={handleMenu}
            color="inherit"
          >
            <AccountCircle />
          </IconButton>
          <Menu
            id="menu-appbar"
            anchorEl={anchorEl}
            anchorOrigin={{
              vertical: 'top',
              horizontal: 'right',
            }}
            open={Boolean(anchorEl)}
            onClose={handleClose}
          >
            <MenuItem onClick={handleClose}>予約確認</MenuItem>
            <MenuItem onClick={handleClose}>来店履歴</MenuItem>
            <MenuItem onClick={handleClose}>ログアウト</MenuItem>
          </Menu>
        </Toolbar>          
      </AppBar>
    </Box>
    
  )
}
