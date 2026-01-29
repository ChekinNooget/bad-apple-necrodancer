--importing modules
local Tile = require "necro.game.tile.Tile"
local Soundtrack = require "necro.game.data.Soundtrack"
local CurrentLevel = require "necro.game.level.CurrentLevel"
local Music = require "necro.audio.Music"

--music setup
--to be honest im not entirely sure how it works
--but i copied the template from another mod and this is how i got it to work
--/shruggie
local EvilFruitMusic = {}

--there are probably better tiles or i could have made my own white/black sprites
--but i think it looks cool
local tileBright = 212 --ice
local tileDark = 204 --hot coals

--load the table with every pixel
local data = require("EvilFruit.dataFile")

--this is in order to center the animation at 0,0
local offsetX = math.floor(#data[1][1]/2) + 1
local offsetY = math.floor(#data[1]/2) + 1

--this runs every beat
event.turn.add("updateTile", {order="minimap"}, function(ev)
    --the music doesn't start at 0 because of the disco descent fakeout, so offset it
    local realMusicTime = Music.getMusicTime() - 7.59293
    --this is the frame number, we need to calculate it so that late mp joiners are on the right beat (because lots of people will play this mod in multiplayer im sure)
    --4 comes from bolt + double tempo, used from the python code
    --actually im surprised, i just tested and it actually syncs to the music in regular tempo or double tempo :O
    --but the fps is too slow to be good
    local beatNumber = math.floor(2.3*4*realMusicTime) + 1
    --dont run it in the lobby or it'll ruin the surprise!
    if not CurrentLevel.isLobby() then
        --only start rendering frames if the music actually begins
        if beatNumber > 0 then
            --hardcoded number of frames because #length doesn't work, idk why lol
            --it's fiiine
            if beatNumber <= 1993 then
                --set each pixel in a grid
                for i = 1, #data[1][1], 1 do
                    for j = 1, #data[1], 1 do
                        setTile(i - offsetX, j - offsetY, data[beatNumber][j][i])
                    end
                end
            end
        end
    end
end)

--setup music only if it isn't the lobby
event.musicTrack.add("EvilFruitMusic", "zone", function (ev)
    if not CurrentLevel.isLobby() then
        ev.beatmap = "mods/EvilFruit/music/beatmap.txt"
        ev.originalBeatmap = "mods/EvilFruit/music/beatmap.txt"
        ev.loop = false
        
        ev.layers[#ev.layers + 1] = {
            beatmap="mods/EvilFruit/music/beatmap.txt",
            originalFile = "mods/EvilFruit/music/song.ogg",
            file = "mods/EvilFruit/music/song.ogg",
            type = Soundtrack.LayerType.MAIN,
        }
    end
end)
event.levelLoad.add("setMusic", {order="lobbyLevel"}, function(ev)
    if not CurrentLevel.isLobby() then
        Music.setMusic({type = EvilFruitMusic.MusicType})
    end
end)

--explains itself; 1 means white, 0 means black
function setTile(x, y, tileType)
    if tileType == 1 then
        Tile.set(x, y, tileBright)
    else
        Tile.set(x, y, tileDark)
    end
end