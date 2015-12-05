pro twopulse

; define velocity and time vectors
  x= [-10.0,-2.0,-1.5,-1.0, 1.0, 1.5, 2.0,10.0]
  y= [  0.0, 0.0, 0.25,0.0, 0.0,-0.25,0.0, 0.0]

; setup postscript plot
  !P.FONT= -1 & !P.BACKGROUND= 255 & !P.COLOR= 0
  set_plot, "PS"
  xsize= 7.5 & ysize= 3.0
  device, file='twopulse.eps',/inches,xsize=xsize,ysize=ysize, $
    xoffset=(8.5-xsize)/2.0,yoffset=(11.0-ysize)/2.0,/color,bits_per_pixel=24
  !P.THICK= 4.0
  !P.CHARTHICK= !P.THICK & !X.THICK= !P.THICK & !Y.THICK= !P.THICK
  !P.CHARSIZE= 1.2
  !X.CHARSIZE= !P.CHARSIZE & !Y.CHARSIZE= !P.CHARSIZE
  !P.PSYM= 0
  !P.TITLE= ''
  !X.STYLE= 1
  !X.TITLE= ''
  !X.RANGE= [-3.0,3.0]
  !X.MARGIN= [7,0]
  !X.OMARGIN= [1,1]
  !X.TICKLEN= 1.0
  !Y.STYLE= 1
  !Y.TITLE= ''
  !Y.RANGE= [-1.0,1.0]
  !Y.MARGIN= 0.6*!X.MARGIN
  !Y.OMARGIN= 0.6*!X.OMARGIN
  !Y.TICKLEN= 1.0
  !P.MULTI= 0
  xyouts, 0,0,'!3'

; plot
  djs_plot, x,y,thick=16,xtitle='!8x!3  (m)',ytitle='!8y!3  (m)'

; label
  djs_xyouts, -1.5,0.35,'A',align=0.5,charsize=2.0
  djs_xyouts,  1.5,0.35,'B',align=0.5,charsize=2.0
  xarrow= [1.8,1.2,1.3,1.2,1.3]
  yarrow= [0.0,0.0,0.1,0.0,-0.1]
  djs_oplot, xarrow,yarrow+0.2
  djs_oplot, -xarrow,yarrow-0.2

; close
  device,/close
  return
end
