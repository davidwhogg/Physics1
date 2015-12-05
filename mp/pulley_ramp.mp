% ramp, pulley and blocks
% 2001-Oct-15  written by Hogg

beginfig(1) ;
  u=1.0cm ;

% define pen weights
  numeric axis_pen_weight ;
  numeric curve_pen_weight ;
  numeric dot_pen_weight ;
  numeric vector_pen_weight ;
  axis_pen_weight=     1.0 ;
  curve_pen_weight=    2.0 ;
  support_pen_weight=  4.0 ;
  dot_pen_weight=      4.0 ;

% draw blocks
  pickup pencircle scaled curve_pen_weight ;
  draw (-5u,0)--(0,0)--(3u,1.5u)--(3u,0)--(8u,0) ;
  draw (0.8u,0.4u)--(0.4u,1.2u)--(1.2u,1.6u)--(1.6u,0.8u)--cycle ;
  draw (3.2u,0.4u)--(4.0u,0.4u)--(4.0u,1.2u)--(3.2u,1.2u)--cycle ;

% draw pulley and strings
  rad= 0.3u ;
  cosine= 2/sqrt(5) ;
  sine= 1/sqrt(5) ;
  z1= (3.6u-rad,0.5(3.6u-rad)+0.4u-rad*cosine) ;
  draw (-rad,0)..(0,rad)..(rad,0)..(0,-rad)..cycle shifted z1 ;
  draw (3.6u,1.2u)--(z1+(rad,0)) ;
  draw (1.4u,1.2u)--(z1+rad*(-sine,cosine)) ;

% draw support
  pickup pencircle scaled support_pen_weight ;
  draw (3u,1.5u)--z1 ;

% draw joints
  pickup pencircle scaled dot_pen_weight ;
  draw (1.4u,1.2u) ;
  draw (3.6u,1.2u) ;
  draw z1 ;

% draw axes
  sinhalf= sqrt((1-cosine)/2) ;
  coshalf= sqrt((1+cosine)/2) ;
  pickup pencircle scaled axis_pen_weight ;
  draw (u,0)..(u*coshalf,u*sinhalf)..(u*cosine,u*sine) ;
  draw (0,0)--(1.5u,0) ;

% place labels
  label(btex $m_1$ etex, (1.0u,1.0u)) ;
  label(btex $m_2$ etex, (3.6u,0.8u)) ;
  label.rt(btex $\theta$ etex, (u*coshalf,u*sinhalf)) ;

endfig ;
end
