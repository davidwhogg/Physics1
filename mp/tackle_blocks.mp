% tackle blocks
% 2001-Oct-03  written by Hogg

beginfig(1) ;
  u=1.00cm ;

% define pen weights
  numeric axis_pen_weight ;
  numeric curve_pen_weight ;
  numeric dot_pen_weight ;
  numeric vector_pen_weight ;
  axis_pen_weight=     0.5 ;
  curve_pen_weight=    2.0 ;
  dot_pen_weight=      6.0 ;

% draw ceiling, blocks and strings
  pickup pencircle scaled curve_pen_weight ;
  draw (-u,0)--(3.5u,0) ;
  draw (0,0)--(0,-4u) ;
  draw (u,-4u)--(u,-2u) ;
  draw (2u,-2u)--(2u,-5u) ;
  draw (0.5u,-4u)--(0.5u,-5u) ;
  draw (1.5u,-2u)--(1.5u,0) ;
  draw (0,-5u)--(u,-5u)--(u,-6u)--(0,-6u)--cycle ;
  draw (1.5u,-5u)--(2.5u,-5u)--(2.5u,-6u)--(1.5u,-6u)--cycle ;

% draw pulleys
  draw (0,-4u)..(0.5u,-3.5u)..(u,-4u)..(0.5u,-4.5u)..cycle ;
  draw (u,-2u)..(1.5u,-1.5u)..(2u,-2u)..(1.5u,-2.5u)..cycle ;

% draw joints
  pickup pencircle scaled dot_pen_weight ;
  draw (0,0) ;
  draw (1.5u,0) ;
  draw (0.5u,-4u) ;
  draw (1.5u,-2u) ;
  draw (0.5u,-5u) ;
  draw (2u,-5u) ;
  
% write labels
  label(btex $m_1$ etex, (0.5u,-5.5u)) ;
  label(btex $m_2$ etex, (2u,-5.5u)) ;
  
endfig ;
end
