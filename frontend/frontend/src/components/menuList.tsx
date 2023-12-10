import React from 'react';
import Grid from '@mui/material/Grid';
import { MenuCard } from './menuCard';
import SimpleDesignImage from '../images/simple_design.jpg';
import OneColorImage from '../images/one_color.jpg';

export const MenuList = () => {
  const menus = [
    {
      menu: 'simple design',
      duration: '120分',
      price: '¥6,600',
      image: SimpleDesignImage
    },
    {
      menu: 'one color',
      duration: '90分',
      price: '¥6,600',
      image: OneColorImage
    }
  ];

  // MenuCardが一行に一つ配置されるように修正する
  return (
    <Grid container spacing={2} justifyContent='center'>
      {menus.map((item, index) => {
        return (
          <Grid item key={index} xs={10} sm={8}>
            <MenuCard {...item} />
          </Grid>
        )
      })} 
    </Grid>
  )
}
