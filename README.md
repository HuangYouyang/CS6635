# CS6635
Final Project for CS6635

- [x] matplotlib particle_density_2d (animation + image) 
  - `./matplotlib/particle_density_2d.py`
  - `particle_density(startT, endT, animation=False, save=True, twoD=True)`
    - `time`: [0.12, 0.99]
    - `twoD`: if True, it shows the 2D scatter result; if False, it shows the 3D scatter result. (3D动画需要很长时间)
- [x] raw particles 数据转成VTK对象（position，velocity，acceleration，gravitational potential-phi）
- [ ] halo 数据转成VTK对象（haloId，time，scale）（还有点问题）

最终结果图
1. 2D Projection of Particle Density (animation)
  ![ParticleDensity2D_GIF](output/ParticleDensity/particle_density_2d.gif)
2. 3D Projection of Particle Density (static)
  ![ParticleDensity3D](output/ParticleDensity/particle_density_3d_0.png)
3. Gravitational potential of particles Over Time
   ![Phi](output/ParticleAttributesRelationOverTime/Phi_0.3.png)
   ![Phi](output/ParticleAttributesRelationOverTime/Phi_0.7.png)
   ![Phi](output/ParticleAttributesRelationOverTime/Phi_1.0.png)
4. Acceleration of particles Over Time
   ![Phi](output/ParticleAttributesRelationOverTime/Acc_0.3.png)
   ![Phi](output/ParticleAttributesRelationOverTime/Acc_0.7.png)
   ![Phi](output/ParticleAttributesRelationOverTime/Acc_1.0.png)
5. Velocity of particles Over Time
   ![Phi](output/ParticleAttributesRelationOverTime/V_0.3.png)
   ![Phi](output/ParticleAttributesRelationOverTime/V_0.7.png)
   ![Phi](output/ParticleAttributesRelationOverTime/V_1.0.png)