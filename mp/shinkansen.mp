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
  vector_pen_weight=   3.0 ;

% draw wheels
  pickup pencircle scaled curve_pen_weight ;
  wrad= 0.3u ;
  path wheel ;
  wheel= (-wrad,0)..(0,wrad)..(wrad,0)..(0,-wrad)..cycle ;
  draw wheel shifted (3u,wrad-0.2u) ;
  draw wheel shifted (4u,wrad-0.2u) ;
  draw wheel shifted (5u,wrad-0.2u) ;
  draw wheel shifted (6u,wrad-0.2u) ;
  clip currentpicture to (0,0)--(0,-0.2u)--(8u,-0.2u)--(8u,0)--cycle ;
  
% draw tracks, train and ball
  pickup pencircle scaled curve_pen_weight ;
  path shinkansen ;
  shinkansen= (8u,0)--(0.2u,0)--(0.2u,0.2u)--(2u,2u)--(8u,2u) ;
  draw shinkansen ;
  draw (-3u,-0.2u)--(8u,-0.2u) ;
  rad= 0.1u ;
  draw (0-rad,u)..(0,u+rad)..(0+rad,u)..(0,u-rad)..cycle ;

% draw vectors
  pickup pencircle scaled vector_pen_weight ;
  drawarrow (1.8u,1.8u)--(-2u,1.8u) ;

% draw axes
  cosine= 1.0/sqrt(2.0) ;
  sine= 1.0/sqrt(2.0) ;
  sinhalf= sqrt((1-cosine)/2) ;
  coshalf= sqrt((1+cosine)/2) ;
  pickup pencircle scaled axis_pen_weight ;
  draw (u,0)..(u*coshalf,u*sinhalf)..(u*cosine,u*sine) ;

% place labels
  label.rt(btex $\theta$ etex, (u*coshalf,u*sinhalf)) ;
  label.bot(btex $v_S$ etex, (-u,1.8u)) ;
  label.lft(btex $m$ etex, (0-rad,u)) ;
  label.lft(btex $M$ etex, (3u,u)) ;

endfig ;
end
