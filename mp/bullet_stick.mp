% bullet and stick
% 2007-12-19  written by Hogg

beginfig(1) ;
  u=1.5cm ;

% define pen weights
  numeric axis_pen_weight ;
  numeric vector_pen_weight ;
  numeric curve_pen_weight ;
  numeric dot_pen_weight ;
  axis_pen_weight=     0.5 ;
  vector_pen_weight=   0.75 ;
  curve_pen_weight=    1.0 ;
  dot_pen_weight=      2.0 ;

% draw stick
  pickup pencircle scaled curve_pen_weight ;
  draw (0,0)--(0,2u)--(0.2u,2u)--(0.2u,0)--cycle ;

% draw bullet
  pickup pencircle scaled dot_pen_weight ;
  draw (-1.6u,2u) ;

% draw velocity
  pickup pencircle scaled vector_pen_weight ;
  drawarrow (-1.5u,2u)--(-0.6u,2u) ;

% draw labels
  label.bot(btex $m$ etex, (-1.6u,2u)) ;
  label.bot(btex $v$ etex, (-1.0u,2u)) ;
  label.rt(btex $m,\ell$ etex, (0.2u,u)) ;

endfig ;
end
