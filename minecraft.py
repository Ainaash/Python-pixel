import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc=minecraft.Minecraft.create()

player_pos=mc.player.getTilePos()

farm_width=10
farm_length=10
farm_height=1
farm_pos_x=player_pos.x+1
farm_pos_y=player_pos.y
farm_pos_z=player_pos.z+1

mc.setBlocks(farm_pos_x-1,farm_pos_y-1, farm_pos_z-1, farm_pos_x+farm_width,farm_pos_y-1, farm_pos_z+farm_length,block.GLASS.id)

mc.setBlocks(farm_pos_x,farm_pos_y-1, farm_pos_z, farm_pos_x+farm_width-1,farm_pos_y-1, farm_pos_z+farm_length-1,block.GRASS.id)

for y in range(farm_pos_y,farm_pos_y+farm_height):
    for x in range (farm_pos_x-1, farm_pos_x+farm_width+1):
        mc.setBlock(x,y,farm_pos_z-1, block.FENCE.id)
        mc.setBlock(x, y, farm_pos_z+farm_length.block.FENCE.id)
    for z in range (farm_pos_z-1,farm_pos_z+farm_length+1):
        mc.setBlock(farm_pos_x-1,y,z,block.FENCE.id)
        mc.setBlock(farm_pos_x +farm_width, y, z, block.FENCE.id)

activation_block_x=farm_pos_x+1
activation_block_y=farm_pos_y-1
activation_block_z=farm_pos_z+1

mc.setBlock(activation_block_x,activation_block_y,activation_block_z,block.GLOWSTONE_BLOCK.id)

farm_active=False

while True:
    player_pos=mc.player.getTilePos()

    if (player_pos.x, player_pos.y, player_pos.z)==(activation_block_x,activation_block_y,activation_block_z):
        farm_active=True
        mc.PostToChat("Ферма камня активирована")

        for i in range(100):
            mc.setBlock(activation_block_x+3,activation_block_y+1+i,activation_block_z,block.STONE.id)
            time.sleep(1)
        else:
            farm_active=False
            mc.postToChat("Ферма камня деактивирована")

        time.sleep(0.1)


