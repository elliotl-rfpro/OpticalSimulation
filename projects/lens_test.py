import KrakenOS as Kos


def example_adas_camera_system():
    sequence = []

    # Object plane
    P_Obj = Kos.surf()
    P_Obj.Rc = 0.0
    P_Obj.Thickness = 10.0
    P_Obj.Glass = "AIR"
    P_Obj.Diameter = 50.0
    P_Obj.Name = "Object Plane"
    sequence.append(P_Obj)

    # Lens 1: In
    s1_1 = Kos.surf()
    s1_1.Rc = 28.878
    s1_1.Thickness = 2.0
    s1_1.Diameter = 11.962
    s1_1.Glass = 'F2'
    # s1_1.Name = 'S1_1'
    sequence.append(s1_1)

    # Lens 1: Out
    s1_2 = Kos.surf()
    s1_2.Rc = 15.715
    s1_2.Thickness = 2.210
    s1_2.Diameter = 11.232
    s1_2.Glass = 'AIR'
    # s1_2.Name = 's1_2'
    sequence.append(s1_2)

    # Lens 2: In
    s2_1 = Kos.surf()
    s2_1.Rc = -43.671
    s2_1.Thickness = 4.996
    s2_1.Diameter = 11.054
    s2_1.Glass = 'BK7'
    # s2_1.Name = 's2_1'
    sequence.append(s2_1)

    # Lens 2: Out
    s2_2 = Kos.surf()
    s2_2.Rc = -15.704
    s2_2.Thickness = 0.820
    s2_2.Diameter = 10.974
    s2_2.Glass = 'AIR'
    # s2_2.Name = 's2_2'
    sequence.append(s2_2)

    # Lens 3: In
    s3_1 = Kos.surf()
    s3_1.Rc = 20.033
    s3_1.Thickness = 3.716
    s3_1.Diameter = 12.55
    s3_1.Glass = 'F2'
    # s3_1.Name = 's3_1'
    sequence.append(s3_1)

    # Lens 3: Out
    s3_2 = Kos.surf()
    s3_2.Rc = -28.297
    s3_2.Thickness = 0.1
    s3_2.Diameter = 12.67
    s3_2.Glass = 'AIR'
    # s3_2.Name = 's3_2'
    sequence.append(s3_2)

    # Lens 4: In
    s4_1 = Kos.surf()
    s4_1.Rc = 10.894
    s4_1.Thickness = 4.3835
    s4_1.Diameter = 12.15
    s4_1.Glass = 'F2'
    # s4_1.Name = 's4_1'
    sequence.append(s4_1)

    # Lens 5: In
    s5_1 = Kos.surf()
    s5_1.Rc = 0.0
    s5_1.Thickness = 2.0
    s5_1.Diameter = 12.15
    s5_1.Glass = 'F2'
    # s5_1.Name = 's5_1'
    sequence.append(s5_1)

    # Lens 5: Out
    s5_2 = Kos.surf()
    s5_2.Rc = 97.748
    s5_2.Thickness = 2.126
    s5_2.Diameter = 8.404
    s5_2.Glass = 'AIR'
    s5_2.Name = 's5_2'
    # sequence.append(s5_2)

    # Air gap
    g_1 = Kos.surf()
    g_1.Rc = 24.784
    g_1.Thickness = 2.126
    g_1.Diameter = 8.716
    g_1.Glass = 'AIR'
    # g_1.Name = 'g_1'
    sequence.append(g_1)

    # Lens 6: In
    s6_1 = Kos.surf()
    s6_1.Rc = 24.784
    s6_1.Thickness = 2.126
    s6_1.Diameter = 8.716
    s6_1.Glass = 'F2'
    # s6_1.Name = 's6_1'
    sequence.append(s6_1)

    # Lens 6: Out
    s6_2 = Kos.surf()
    s6_2.Rc = -258.549
    s6_2.Thickness = 0.0
    s6_2.Diameter = 8.35
    s6_2.Glass = 'AIR'
    # s6_2.Name = 's6_2'
    # sequence.append(s6_2)

    # Air gap
    g_2 = Kos.surf()
    g_2.Rc = 0.0
    g_2.Thickness = 0.906
    g_2.Diameter = 8.35
    g_2.Glass = 'AIR'
    # g_2.Name = 'g_2'
    sequence.append(g_2)

    # Lens 7: In
    s7_1 = Kos.surf()
    s7_1.Rc = 27.385
    s7_1.Thickness = 2.0
    s7_1.Diameter = 8.284
    s7_1.Glass = 'F2'
    # s7_1.Name = 's7_1'
    sequence.append(s7_1)

    # Lens 7: Out
    s7_2 = Kos.surf()
    s7_2.Rc = 14.711
    s7_2.Thickness = 0.303
    s7_2.Diameter = 9.208
    s7_2.Glass = 'AIR'
    # s7_2.Name = 's7_2'
    # sequence.append(s7_2)

    # Air gap
    g_3 = Kos.surf()
    g_3.Rc = 0.0
    g_3.Thickness = 2.5
    g_3.Diameter = 9.474
    g_3.Glass = 'AIR'
    # g_3.Name = 'g_3'
    sequence.append(g_3)

    # # Pupil
    # pupil_a = Kos.surf()
    # pupil_a.Rc = 0
    # pupil_a.Thickness = 0.340
    # pupil_a.Glass = "AIR"
    # pupil_a.Diameter = 9.474
    # pupil_a.Name = "Pupil"
    # sequence.append(pupil_a)

    # Image plane
    p_ima = Kos.surf()
    p_ima.Rc = 0.0
    p_ima.Thickness = 0.0
    p_ima.Glass = "AIR"
    p_ima.Diameter = 9.474
    p_ima.Name = "Image Plane"
    sequence.append(p_ima)

    # Setup system
    config_1 = Kos.Setup()
    optical_sys = Kos.system(sequence, config_1)
    ray_sys = Kos.raykeeper(optical_sys)

    # Define pupil/aperture
    w = 0.55
    sup = 4
    aper_val = 6
    aper_type = "STOP"
    pupil = Kos.PupilCalc(optical_sys, sup, w, aper_type, aper_val)

    pupil.Samp = 10
    pupil.Ptype = "fany"
    pupil.FieldType = "angle"
    pupil.FieldY = 0.0
    x, y, z, l, m, n = pupil.Pattern2Field()
    for i in range(0, len(x)):
        p_source_0 = [x[i], y[i], z[i]]
        d_cos = [l[i], m[i], n[i]]
        optical_sys.Trace(p_source_0, d_cos, w)
        ray_sys.push()

    pupil.Samp = 10
    pupil.Ptype = "fany"
    pupil.FieldType = "angle"
    pupil.FieldY = 20.0
    x, y, z, l, m, n = pupil.Pattern2Field()
    for i in range(0, len(x)):
        p_source_0 = [x[i], y[i], z[i]]
        d_cos = [l[i], m[i], n[i]]
        optical_sys.Trace(p_source_0, d_cos, w)
        ray_sys.push()

    # Plot
    Kos.display3d(optical_sys, ray_sys,2)
    Kos.display2d(optical_sys, ray_sys, 0, 1)


if __name__ == '__main__':
    print('----- WARNING ! -----')
    print('Please consider that glass types, coatings, Abbe number etc. may not be fully modelled yet!')
    example_adas_camera_system()

    print('Script completed successfully.')
