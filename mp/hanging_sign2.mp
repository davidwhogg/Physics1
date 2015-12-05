% hanging sign
% 2001-Sep-25  written by Hogg
% 2013-Nov-10  re-parameterized

beginfig(1) ;
  u=0.50cm ;

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

% draw wall, beam, sign, pivot, cables
  pickup pencircle scaled curve_pen_weight ;
  draw (-0.5u,-5u)--(-0.5u,8.5u)--(0,8.5u)--(0,9u) ;
  draw (-0.5u,-0.5u)--(0,-0.5u)..(0.5u,0)..(0,0.5u)--(-0.5u,0.5u) ;
  draw (0,0.5u)--(6u,0.5u)--(6u,-0.5u)--(0u,-0.5u) ;
  draw (0,8.5u)--(6u,0.5u) ;
  draw (6u,-0.5u)--(6u,-2u) ;
  draw (5.5u,-2u)--(6.5u,-2u)--(6.5u,-5u)--(5.5u,-5u)--cycle ;

% draw joints
  pickup pencircle scaled dot_pen_weight ;
  draw (0,0) ;
  draw (0,8.5u) ;
  draw (6u,0.5u) ;
  draw (6u,-0.5u) ;
  draw (6u,-2u) ;

% draw measuring bars
  pickup pencircle scaled axis_pen_weight ;
  drawdblarrow (0,-1u)--(6u,-1u) ;

% write labels
  label(btex $m_{\rm b}$ etex, (3u,0)) ;
  label(btex $m_{\rm s}$ etex, (6u,-3.5u)) ;
  label.urt(btex $T_1$ etex, (3u,4.5u)) ;
  label.rt(btex $T_2$ etex, (6u,-1.25u)) ;
  label.bot(btex $L$ etex, (3u,-1u)) ;
  label.bot(btex $\theta$ etex, (4u,2u)) ;

endfig ;
end
