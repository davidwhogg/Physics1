% pedagogical machine
% 2001-Sep-25  written by Hogg

beginfig(1) ;
  u=0.8cm ;

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
  draw (0,0)--(10u,0) ;
  draw (2u,0)--(2u,3u)--(5u,3u)--(5u,0.5u)--(6u,0.5u)--(6u,3u)--
    (7u,3u)--(7u,0) ;
  draw (2.5u,3u)--(2.5u,4u)--(3.5u,4u)--(3.5u,3u)--cycle ;
  draw (5u,1.35u)--(5u,2.35u)--(6u,2.35u)--(6u,1.35u)--cycle ;

% draw pulley and strings
  draw (5.5u,3.25u)..(5.25u,3.5u)..(5.0u,3.25u)..(5.25u,3.0u)..cycle ;
  draw (5u,3u)..(5.25u,3.25u) ;
  draw (5.5u,2.35u)--(5.5u,3.25u) ;
  draw (3.5u,3.5u)--(5.25u,3.5u) ;
  drawarrow (7u,1u)--(8.5u,1u) ;

% draw joints
  pickup pencircle scaled dot_pen_weight ;
  draw (3.5u,3.5u) ;
  draw (5.5u,2.35u) ;
  draw (5.25u,3.25u) ;
  draw (7u,1u) ;

% place labels
  label(btex $m_1$ etex, (3u,3.5u)) ;
  label(btex $m_2$ etex, (5.5u,1.85u)) ;
  label(btex $m_3$ etex, (3.5u,1.5u)) ;
  label.rt(btex $F$ etex, (8.5u,1u)) ;

endfig ;
end
