hom=int(input('Hány fokos a víz? '))
if hom<=0:
    print('A víz szilárd halmazállapotú')
elif 0<hom<100:
    print('A víz folyékony halmazállapotú')
else:
    print('A víz gáz halmazhállapotú')