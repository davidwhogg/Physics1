pro spring_energy

; define time and position vectors
tt= 0d0+0.01*dindgen(2001)
xx= 0.05*cos(0.7*tt+0.4)

; setup postscript plot
!P.FONT= -1 & !P.BACKGROUND= 255 & !P.COLOR= 0
set_plot, "PS"
xsize= 6.0 & ysize= 7.0
device, file='spring_energy.eps',/inches,xsize=xsize,ysize=ysize, $
  xoffset=(8.5-xsize)/2.0,yoffset=(11.0-ysize)/2.0,/color,bits_per_pixel=24
!P.THICK= 2.0
!P.CHARTHICK= !P.THICK & !X.THICK= !P.THICK & !Y.THICK= !P.THICK
!P.CHARSIZE= 1.2
!X.CHARSIZE= !P.CHARSIZE & !Y.CHARSIZE= !P.CHARSIZE
!P.PSYM= 0
!P.TITLE= ''
!X.STYLE= 1
!X.TITLE= ''
!X.MARGIN= [2,2]
!X.OMARGIN= [8,0]
!X.TICKLEN= 1.0
!Y.STYLE= 1
!Y.TITLE= ''
!Y.MARGIN= 0.6*!X.MARGIN
!Y.OMARGIN= 0.6*!X.OMARGIN
!Y.TICKLEN= 1.0
!P.MULTI= [0,1,4]
xyouts, 0,0,'!3'

; plot
plot, tt,xx,thick=4, $
  ytitle='!8x!3  (m)'
plot, tt,xx,/nodata, $
  ytickinterval=100,ytitle='!8K!3  (J)'
plot, tt,xx,/nodata, $
  ytickinterval=100,ytitle='!8U!3  (J)'
plot, tt,xx,/nodata, $
  xtitle='!8t!3  (s)', $
  ytickinterval=100,ytitle='!8E=K+U!3  (J)'

; close
device,/close
return
end
