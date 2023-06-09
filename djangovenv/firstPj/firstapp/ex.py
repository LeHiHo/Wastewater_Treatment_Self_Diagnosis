from typing import Sized
import schemdraw
from schemdraw import flow
from schemdraw.elements.elements import Label
from models import Wastedata
from schemdraw import Drawing, ImageFormat
import matplotlib


BOD_set_RM = 70
TSS_set_RM = 60
TN_set_RM = 70
TP_set_RM = 80

BOD_eff_RM = 70
TSS_eff_RM = 60
TN_eff_RM =  80
TP_eff_RM = 70



matplotlib.use('Agg') # Set the backend here



# 유입수질, 방류수질 입력
d = schemdraw.Drawing(font="d2coding", fontsize= 9)
d += flow.Start(w=13, h=3, label="유입수질, 방류수질 입력")
d += flow.Arrow().down().length(d.unit)


# 제거율 > 목표제거율 ?
d += (BOD_D1 := flow.Decision(w=18, h=7, S="YES", E="NO", label="BOD : 제거율 > 목표제거율 ?"))
d += flow.Arrow(headwidth=1,headlength=1).length(d.unit*2)
d += (TSS_D1 := flow.Decision(w=18, h=7, S="YES", E="NO", label="TSS : 제거율 > 목표제거율 ?"))
d += flow.Arrow(headwidth=1,headlength=1).length(d.unit*3)
d += (TN_D1 := flow.Decision(w=18, h=7, S="YES", E="NO", label="T-N : 제거율 > 목표제거율 ?"))
d += flow.Arrow(headwidth=1,headlength=1).length(d.unit*3)
d += (TP_D1 := flow.Decision(w=18, h=7, S="YES", E="NO", label="T-P : 제거율 > 목표제거율 ?"))
d += flow.Arrow(headwidth=1,headlength=1).length(d.unit)

# 진단완료
d += flow.Start(w=6, h=3, label="진단완료")

# BOD
if BOD_eff_RM <= BOD_set_RM:
    d += flow.Arrow(headwidth=1,headlength=1).right().at(BOD_D1.E).length(d.unit*2).color('Red')
else:
    d += flow.Arrow(headwidth=1,headlength=1).right().at(BOD_D1.E).length(d.unit*2).color('Black')

d += (BOD_D2 := flow.Decision(w=15, h=7, S="YES", E="NO").anchor('W').label("생물반응조 유입수의\nBOD가 고농도?"))

d += flow.Arrow(headwidth=1,headlength=1).down().at(BOD_D2.S).length(d.unit*0.7)
d += (BOD_B1 := flow.Box(w=17, h=3).anchor('N').label("[원인] 고농도 BOD 유입\n[조치] 호기조 송풍량 증량"))

d += flow.Arrow(headwidth=1,headlength=1).right().at(BOD_D2.E).length(d.unit*2.5)
d += (BOD_B2 := flow.Box(w=15, h=3).anchor('W').label("[원인] MLSS 적정범위 이탈\n[조치] 슬러지 반송량 조절"))

# TSS
if TSS_eff_RM <= TSS_set_RM:
    d += flow.Arrow(headwidth=1,headlength=1).right().at(TSS_D1.E).length(d.unit*2).color('Red')
else:
    d += flow.Arrow(headwidth=1,headlength=1).right().at(TSS_D1.E).length(d.unit*2).color('Black')

d += (TSS_D2 := flow.Decision(w=15, h=7, S="YES", E="NO").anchor('W').label("생물반응조 유입수의\nTSS가 고농도?"))
d += flow.Arrow(headwidth=1,headlength=1).down().at(TSS_D2.S).length(d.unit)

d += (TSS_B1 := flow.Box(w=27, h=5).anchor('N').label("[원인] 침사지, 일차침전지, 반류수 처리계통 이상\n[조치] 침사지, 일차침전지, 반류수 처리계통 조치"))
d += flow.Arrow(headwidth=1,headlength=1).right().at(TSS_D2.E).length(d.unit*4)

d += (TSS_D3 := flow.Decision(w=15, h=7, S="YES", E="NO").anchor('W').label("반송슬러지의\nTSS가 고농도?"))
d += flow.Arrow(headwidth=1,headlength=1).down().at(TSS_D3.S).length(d.unit)

d += (TSS_B2 := flow.Box(w=20, h=5).anchor('N').label("[원인] 이차침전지의 과다한 슬러지 축적\n[조치] 슬러지 인발량 증량"))
d += flow.Arrow(headwidth=1,headlength=1).right().at(TSS_D3.E).length(d.unit)

d += (TSS_B3 := flow.Box(w=27, h=5).anchor('W').label("[원인] 슬러지 침강성 불량\n[조치]1 호기조 DO농도 1.0mg/L 유지\n[조치]2 슬러지반송량 조절로 적정 MLSS 유지"))

# T-N
if TN_eff_RM <= TN_set_RM:
    d += flow.Arrow(headwidth=1,headlength=1).right().at(TN_D1.E).length(d.unit*2).color('Red')
else:
    d += flow.Arrow(headwidth=1,headlength=1).right().at(TN_D1.E).length(d.unit*2).color('Black')

d += (TN_D2 := flow.Decision(w=15, h=7, S="YES", E="NO").anchor('W').label("생물반응조 유출수의\n암모니아성 질소 과다?"))

d += flow.Arrow(headwidth=1,headlength=1).down().at(TN_D2.S).length(d.unit)
d += (TN_B1 := flow.Box(w=25, h=5).anchor('N').label("[원인] 질산화 불량\n[조치]1 호기조 송풍량 증량\n[조치]2 슬러지 반송량 조절로 적정 MLSS 유지"))

d += flow.Arrow(headwidth=1,headlength=1).right().at(TN_D2.E).length(d.unit*2.5)
d += (TN_B2 := flow.Box(w=15, h=5).anchor('W').label("[원인] 탈질 불량\n[조치]1 내부반송량 증량\n[조치]2 외부탄소원 공급"))

# T-P
if TP_eff_RM <= TP_set_RM:
    d += flow.Arrow(headwidth=1,headlength=1).right().at(TP_D1.E).length(d.unit*2).color('Red')
else:
    d += flow.Arrow(headwidth=1,headlength=1).right().at(TP_D1.E).length(d.unit*2).color('Black')

d += (TP_D2 := flow.Decision(w=15, h=7, S="YES", E="NO").anchor('W').label("슬러지 인발량 충분?"))

d += flow.Arrow(headwidth=1,headlength=1).down().at(TP_D2.S).length(d.unit)
d += (TP_B1 := flow.Box(w=27, h=7).anchor('N').label("[원인] 인 제거 기작 불량\n[조치]1 혐기조, 호기조 적정 DO 유지\n[조치]2 혐기조 질산성 질소 농도 확인 후 탈질 개선\n[조치]3 MLSS 확인 후 슬러지 반송량 증량"))

d += flow.Arrow(headwidth=1,headlength=1).right().at(TP_D2.E).length(d.unit*2.5)
d += (TP_B2 := flow.Box(w=20, h=5).anchor('W').label("[원인] 슬러지 인발량 불충분\n[조치] 슬러지 인발량 증량"))

drawing = Drawing()

image_bytes = drawing.get_imagedata(ImageFormat.SVG)









