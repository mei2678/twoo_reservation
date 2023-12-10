import React from 'react';
import { Card, CardMedia, CardContent, Typography, CardActions, Button, Box } from '@mui/material';

type Props = {
  image: string;
  menu: string;
  duration: string;
  price: string;
}

export const MenuCard: React.FC<Props> = (menu) => {
  // menuオブジェクトを展開
  const { image, menu: menuName, duration, price } = menu;

  return (
    <Card
      sx={{
        display: 'flex',
        alignItems: 'center',
        padding: 2
      }}
    >
      <CardMedia
        component='img'
        sx={{ 
          width: 150,
          height: 150,
          borderRadius: 5
        }}
        image={image}
        alt={ `${ menuName } image` }
      />
      <CardContent
        sx={{
          flex: '1',
          display: 'flex',
          flexDirection: 'row',
          justifyContent: 'space-between'
        }}
      >
        <Box>
          <Typography component="div" variant="h5">
            { menuName }
          </Typography>
          <Typography variant="subtitle1" color="text.secondary" component="div">
            { duration }
          </Typography>
          <Typography variant="subtitle1" color="text.secondary" component="div">
            { price }
          </Typography>
        </Box>
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center'
          }}
        >
          <Button variant='contained' sx={{ backgroundColor: 'tan' }}>予約</Button>
        </Box>
      </CardContent>      
    </Card>
  )
}
