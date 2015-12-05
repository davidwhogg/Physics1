% rolling on a hilly landscape
% 2002-Nov-09  written by Hogg

beginfig(1) ;
  u=0.6cm ;

% define pen weights
  numeric axis_pen_weight ;
  numeric curve_pen_weight ;
  numeric dot_pen_weight ;
  numeric vector_pen_weight ;
  axis_pen_weight=     0.5 ;
  curve_pen_weight=    2.0 ;
  vector_pen_weight=   1.5 ;
  dot_pen_weight=      4.0 ;
  particle_pen_weight= 6.0 ;

% draw hill
  pickup pencircle scaled curve_pen_weight ;
  z1= (0,3u) ;
  z2= (10u,0) ;
  z3= (15u,u) ;
  z4= (17u,0) ;
  draw z1{dir -45}..z2..{right}z3..z4 ;

% draw hoops
  path hoop ;
  hoop= fullcircle scaled u ;
  z5= (z1 + ((0,u/2) rotated -45)) ;
  z6= (z3 + (0,u/2)) ;
  draw (hoop shifted z5) ;
  draw (hoop shifted z6) ;

% draw axes
  pickup pencircle scaled axis_pen_weight ;
  draw z5--(x4,y5) ;
  drawdblarrow z6--(x6,y5) ;

% place labels
  label.bot(btex A etex,z1) ;
  label.bot(btex B etex,z3) ;
  label.rt(btex $h$ etex,(0.5[z6,(x6,y5)])) ;
endfig ;
end
