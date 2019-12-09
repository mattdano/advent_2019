import bpy
import numpy as np

for o in bpy.context.scene.objects:
    if o.type == 'MESH':
        o.select = True
    else:
        o.select = False

# Call the operator only once
bpy.ops.object.delete()

dat = open('/Users/mattpang/Downloads/advent/input-8.txt','r').readlines()
layers = np.reshape(np.asarray(nums),(100,6,25))
layers = np.reshape(np.asarray(nums),(100,6*25))
layer_fewest_zeros = (layers == 0).sum(axis=1).argmin()

nums = []
for c in dat[0][:-1]:
    nums.append(int(c))
    
layers = np.reshape(np.asarray(nums),(100,6,25))
selected = layers[layer_fewest_zeros,:,:]

part_1_ans = (selected.ravel()==1).sum()*(selected.ravel()==2).sum()
print(part_1_ans)

def which_colour(inputlist):
    for pos,colour in enumerate(inputlist):
        if colour != 2:
            return pos,colour

blank = np.zeros((6,25))

#material properties
black = bpy.data.materials.new(name = 'my_black_material')
 
# Set some properties of the material.
black.diffuse_color = (0., 0., 0.)
black.diffuse_shader = 'LAMBERT' 
black.diffuse_intensity = 1.0 
black.specular_color = (1., 1., 1.)
black.specular_shader = 'COOKTORR'
black.specular_intensity = 0.5
black.alpha = 1
black.ambient = 1

white = bpy.data.materials.new(name = 'my_white_material')
 
# Set some properties of the material.
white.diffuse_color = (1., 1., 1.)
white.diffuse_shader = 'LAMBERT' 
white.diffuse_intensity = 1.0 
white.specular_color = (1., 1., 1.)
white.specular_shader = 'COOKTORR'
white.specular_intensity = 0.5
white.alpha = 1
white.ambient = 1

glass = bpy.data.materials.new(name = 'my_glass_material')
 
# Set some properties of the material.
glass.diffuse_color = (0.5, 0.5, 0.5)
glass.diffuse_shader = 'LAMBERT' 
glass.diffuse_intensity = 1.0 
glass.specular_color = (1., 1., 1.)
glass.specular_shader = 'COOKTORR'
glass.specular_intensity = 0.5
glass.alpha = 0.0
glass.ambient = 1
glass.transparency= True

layers = np.reshape(np.asarray(nums),(100,6,25))
for i in range(0,6):
    for j in range(0,25):
        pos,colour = which_colour(layers[:,i,j])
        mybox = bpy.ops.mesh.primitive_cube_add(location = (i, j, pos))
        bpy.ops.transform.resize(value=(0.5, 0.5, 0.1))
        cube = bpy.context.object
        mesh = cube.data
        if colour == 1:
            mesh.materials.append(white)
        elif colour == 0:
            mesh.materials.append(black)
               
            
                
                
#bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
