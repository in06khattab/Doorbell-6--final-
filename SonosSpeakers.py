import soco
from soco import SoCo

print ('begin')
#import soco.plugins.talk as talk
import soco
from soco import SoCo

speakerSlaapkamer = SoCo('192.168.2.4')
print (speakerSlaapkamer.player_name + ' en ' + speakerSlaapkamer.ip_address)
speakerSlaapkamer.play_uri('DidlMusicTrack beep-02.mp3 at 0x74a7aef0')
speakerWoonkamer = SoCo('192.168.2.5')
print (speakerWoonkamer.player_name + ' en ' + speakerWoonkamer.ip_address)
print (speakerSlaapkamer.get_music_library_information('tracks',search_term='beep')[0])
    
#    speaker.play('http://www.tieka.nl/demos/doorbell/sounds/beep-01.mp3')
#    speaker.play_uri('http://archive.org/download/TenD2005-07-16.flac16/TenD2005-07-16t10Wonderboy_64kb.mp3')
#    print speaker.ip_address

#mp3sound = '/home/pi/doorbell/sounds/beep-01.mp3'
#sonos.pause()
#sonos.play_uri('http://archive.org/download/TenD2005-07-16.flac16/TenD2005-07-16t10Wonderboy_64kb.mp3')
#sonos.play_uri(mp3sound)
#track= sonos.get_current_track()
#print track['title']
#sonos.play_uri(mp3sound)
print ('en klaar')
