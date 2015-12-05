% table, pulley and blocks
% 2002-Oct-19  written by Hogg

beginfig(1) ;
  u=0.8cm ;

% declare variables

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

% draw blocks
  pickup pencircle scaled curve_pen_weight ;
  path block ;
  block = (0,0)--(0,1)--(1,1)--(1,0)--cycle ;
  draw (block scaled u shifted (0,2u)) ;
  draw (block scaled u shifted (5u,0)) ;
  draw (-u,2u)--(5u,2u) ;
  draw (4u,2u)--(4u,-0.5u) ;

% draw pulley and strings
  path pulley ;
  pulley = (1,0)..(0,1)..(-1,0)..(0,-1)..cycle ;
  draw (pulley scaled (0.5u) shifted (5u,2u)) ;
  draw (u,2.5u)--(5u,2.5u) ;
  draw (5.5u,2u)--(5.5u,u) ;

% draw joints
  pickup pencircle scaled dot_pen_weight ;
  draw (u,2.5u) ;
  draw (5.5u,u) ;
  draw (5u,2u) ;

% draw g
  pickup pencircle scaled vector_pen_weight ;
  drawarrow (6.5u,3u)--(6.5u,1.5u) ;

% place labels
  label(btex $m_1$ etex, (0.5u,2.5u)) ;
  label(btex $m_2$ etex, (5.5u,0.5u)) ;
  label.lft(btex $\mu$ etex, (-u,2u)) ;
  label.rt(btex $\vec{g}$ etex, (6.5u,2.5u)) ;

endfig ;
end
