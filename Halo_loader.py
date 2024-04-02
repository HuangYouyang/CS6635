from thingking import loadtxt

class Halo(object):
    def __init__(self, filename):
        self.scale, self.id, self.desc_scale, self.desc_id, self.num_prog, self.pid, self.upid, self.desc_pid, self.phantom, \
        self.sam_mvir, self.mvir, self.rvir, self.rs, self.vrms, self.mmp, self.scale_of_last_MM, self.vmax, self.x, self.y, self.z, \
        self.vx, self.vy, self.vz, self.Jx, self.Jy, self.Jz, self.Spin, self.Breadth_first_ID, self.Depth_first_ID, \
        self.Tree_root_ID, self.Orig_halo_ID, self.Snap_num, self.Next_coprogenitor_depthfirst_ID, \
        self.Last_progenitor_depthfirst_ID, self.Rs_Klypin, self.M_all, self.M200b, self.M200c, self.M500c, \
        self.M2500c, self.Xoff, self.Voff, self.Spin_Bullock, self.b_to_a, self.c_to_a, self.A_x, self.A_y, self.A_z, \
        self.b_to_a_500c, self.c_to_a_500c, self.A_x_500c, self.A_y_500c, self.A_z_500c, self.T_over_U, \
        self.M_pe_Behroozi, self.M_pe_Diemer, self.Macc, self.Mpeak, self.Vacc, self.Vpeak, self.Halfmass_Scale, \
        self.Acc_Rate_Inst, self.Acc_Rate_100Myr, self.Acc_Rate_Tdyn = \
            loadtxt(filename, unpack=True)