% stick and force
% 2004-04-03  written by Hogg

beginfig(1) ;
  u=0.8cm ;

% define pen weights
  numeric axis_pen_weight ;
  numeric curve_pen_weight ;
  numeric dot_pen_weight ;
  numeric vector_pen_weight ;
  axis_pen_weight=     0.5 ;
  curve_pen_weight=    1.0 ;
  vector_pen_weight=   1.0 ;

% draw stick
  pickup pencircle scaled curve_pen_weight ;
  draw (0,0)--(0,2u)--(0.2u,2u)--(0.2u,0)--cycle ;

% draw force
  drawarrow (-u,2u)--(-0.1u,2u) ;

% draw labels
  label.bot(btex $F$ etex, (-0.75u,2u)) ;
  label.rt(btex $m,\ell$ etex, (0.2u,u)) ;

endfig ;
end
