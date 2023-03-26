# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define main = Character("lily")

define mia = Character("Mia")

define granny = Character("Granny")

define dog = Character("Dog")


# The game starts here.

label start:

    play music "audio/Title Theme FULL loop.flac"


    "I was having a dream. A dream of that day... Or perhaps, a memory?"

    "I was sitting on a rooftop near her."

    "The sky was illuminated by the full moon and the numerous stars companying it."

    "I felt joy, as I was glad to be there. I was glad to be with her."
    
    show lily sad night

    main "I wish this moment would last forever, y'know?"

    "I couldn't help but say my thoughts out loud to her"

    mia "..."


    "I turned to look at her. But her face was too blurry to tell."
    
    "My own smile started to fade as I leaned closer to her, trying to see her face more clearly."

    "Her mouth was moving, but I couldn't understand a word she was saying. All her words to me were
    incoherent mumbling."

    "I remember being worried about her."

    
    show lily shocked night

    main "Mia?"

    "She pauses for a moment, before she says something to me. Something I am finally able to hear, and 
    understand"

    mia "The next time... the moon... the stars... Remember... I'll be waiting..."

    "Her whole body started to blur and fadeout even more than her face before, right in front of my eyes."

    "Terrified, I reach out my hand to grab her before it was too late."
    
    main "...MIA!"

    hide lily shocked night

    "My own panicked voice woke me up abruptly. Still half asleep and scared my eyes opened wide to stare up at my empty ceiling."

    "That dream again, huh?"

    "I had a headache and my heart was pounding in my chest. I got up to a sitting position, holding my head 
    and waiting for the pain to subside."


    "Why won't it stop tormenting me?"

    "I could not remember clearly what Mia had said to me just now."

    "I kept dreaming about her for months, which worried me, but she has never talked to me about that message."

    "It was almost as if she was beside me..."

    "But of course, that was impossible. And looking around I could only see my gloomy, dark room. There was no one else there. 
    I looked at the clock on the wall."

    "2AM"

    main "...?"

    "My room was oddly bright, considering how late it still was. It bothered me"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bedroom

    play music "audio/Lily's Room FULL loop.flac"

    
    "I quickly glanced at my window to the left, and I was vexed too see that my curtains were still open."

    # play music "<loop 2>audio/Test.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show lily neutral night 

    "I got off my bed and walked up to the window to close the curtains, but I saw something right outside on my room's windowsill."
    
    main "What is that?"

    "I looked through to see that it seemed to be some type of white bracelet. It was reflecting the moon's 
    light, almost glowing as I looked at it"

    "I lived on the 6th floor, so I had no idea how it had gotten so high up, but it looked important, so I 
    carefully opened my window and took it."

    "I inspected it."

    #inspected 

    "It looked to be made of multiple thin white threads tied or braded together tightly."


    "I didn't know whose it was, but it was very pretty. It would look good on my wrist too and there was no one here."

    main "....?"

    "After contemplating for a minute I placed it gently around my wrist, tightly enough that it wouldn't fall off 
    and get dirty."

    "I waved my hand slowly up and down, and left to right. It went from glowing to gleaming, 
    even brighter than outside, as I had it on my hand."

    "I hadn’t closed my widow yet. I put my head through it to look outside again if I could see anything
    or anyone..."

    main "?"

    show lily shocked night 

    "But instead, I noticed on the spot from which I had taken the bracelet, there was now another small 
    object, I could've sworn hadn't been there a minute ago"

    "I grabbed it too, because I couldn't make out what it was."

    main "What?"

    "Suddenly my vision was filled by pale light coming from the object I was holding."

    "I did not have time to be afraid, since the blinding flash lasted for only a couple of seconds..."


    # These display lines of dialogue.


    # This ends the game.

    jump scene2

    return

label scene2:
    scene interior day one

    play music "audio/Title Theme FULL loop.flac"

    "...And when I regained my sight, I was somewhere completely different"

    main "What just happened?"

    show lily neutral

    "I found myself standing in an old, traditional style japanese house. The room was small and there 
    were no windows."

    "Looking down I could see a small table with two pillows near it. The other pillow was smaller than 
    the other... The room appeared to be for drinking tea or waiting"

    main "Weird, how did I end up here?"

    "One of the walls had a sliding door. I opened and walked through it to find myself in a larger room; 
    probably the main hall of the building."

    "The house was rather sizeable looking. I had to imagine the person who owned it to be pretty 
    wealthy."

    "I was feeling like I was rudely intruding on someone else's private property, so I began looking for 
    an exit"

    "All the windows were covered with shutters, so I ended up stumbling over some things in the dark 
    to get to the door, which had most light coming from behind it"

    "I grabbed the indented handle and pulled the door to the side."

    main "Ah!"

    show lily shocked

    "I was blinded once more, but this time..."

    "It was caused by daylight."

    "The sun was already up, but wasn't it 2am just now?"

    "Confused and still squinting my eyes, I peered from under my raised hand outside, trying to shield 
    my eyes from the bright sunlight."

    scene exterior

    "It took me a second to realize that I was standing in the inner garden, or a type of court of the house."

    "I tried to look around, but I haven't found the actual exit yet."

    "I walked around the garden a little, looking for another door to find the main entrance."

    "While everything looked so well kept and everything, I began to wonder if anyone lived there, 
    because the place looked run-down, with the plants growing over the building."

    "And despite trying not to, I couldn't help but look in awe at the small pond and the flourishing trees 
    and bushes around it, whenever my eyes happened to come accross them"

    main "Wow, so pretty..."

    "I wished the two of us could have a house like this someday."

    play music "audio/GRANDMA FULL loop 2.flac"

    granny "Why thank you dear?"

    show lily shocked at right

    "I jumped from hearing a stranger's voice out of nowhere."

    "Controlled solely by my reflexes I turned to face the person, who was gazing at the garden from a 
    nearby shadow."

    "She looked to be an older woman, her entire body was enveloped in pale hue that reminded me 
    of the moon."

    "And she seemed to be floating"

    "Gazing down I saw that her legs were missing and in their place her body stretched on like a 
    serpentine that became gradually transparent enough to disappear into thin air. I must be dreaming."

    "I rubbed my eyes and looked again. She was still there, meeting my gaze with a warm smile."

    show old lady neutral at left

    granny "Oh-ho, but where are my manners? Welcome to my home, dear. What's your name, 
    dear?"

    main "EAAH!"

    "I shouted out of surprise as she began floating towards me. I tried to quickly move away, but ended 
    up tripping over a stone I didn't see behind me and falling onto my butt."

    show lily sad at right

    "Ow..."

    "Embarrassed and in pain, I peeked at the woman again. She had a puzzled look in her eyes as she 
    looked down at me."

    granny "Are you alright dear?" 

    show lily neutral at right 

    main "Y-yes."

    "I quickly got back onto my feet, trying to stay calm."

    granny "I'm so sorry, I didn't mean to scare you."

    show lily happy at right

    main "...N-no! I'm the one who should be apologizing! M-my name's Lily a-and I swear, I did not 
    mean to be trespassing like this, ma'am...!"

    "I bowed down, but she immediately began gesturing for me to stop."

    show old lady happy at left

    granny "Now now, there is no need to be so tense. You can call me Granny, if you like, Lily. You are not trespassing, dear."

    show lily neutral at right

    main "I am not?"

    "She shook her head."

    granny "Not at all, you're the first visitor I had, I've been waiting for a long time."

    granny "Hmm... There must be something that guided your mind and soul to this place, to me, 
    now that I think about it, dear."

    main "My... Mind and soul? What do you mean by that?"

    "She looked me up and down. I followed her gaze."

    main "Huh?"

    "All my body and the clothes I was wearing were transparentm if you looked carefully enough at me.
    Thankfully I still had my legs and all, but clearly, something wasn't right."
    
    show lily shocked at right 

    "What is this?!"

    granny "Hush-hush, now, don't be so alarmed. This is all but a dream, you are not in harms 
    way...Or I suppose I should say that this is real, yet, it's not."

    main "W-well, that's kind of cryptic, but I guess I kind of understand what you mean. So, I'm not here physically?"

    "She nodded, confirming it. I had to think. I was missing something."

    main "Wait! How was I opening those doors before...?"

    granny "That's more complicated ."    

    main "What do you mean?"

    granny "You see, this place is more of a memory of mine. Something that I haven't been quite 
    able to let go off yet, you see..."

    "This is something similar to the dream I had. She was staring at me."

    show old lady neutral at left

    granny "If you don't mind, could I ask you. What is that you have been holding onto this whole time?"

    main "I don't know what you mean?"

    "She gestured at my hand which had the bracelet on it. I raised it up to my face. I had completely 
    forgotten that I was still holding onto something tightly within my fist. "

    "I opened my hand. It was a silver hairpin, which had an intricate, large tsubaki flower sculpted onto it. She floated closer to look at my hand"

    show old lady happy at left

    granny "Oho! That used to be mine."

    show lily sad at right 

    "I feel bad for taking the bracelet. I thought it would belong to no one, but it did to her. But she didn't seem to blame me 
    She then floated back away from me without any animosity."

    granny "Ahh, but that explains why you arrived here specifically. How intriguing indeed."

    main "You're not angry?"

    granny "I'm not able to make use of it anymore. But now I know why you're here. Keep it."

    "I looked at it, still uncomfortable, before sliding it off."

    granny "It suits you though, so keep it."

    "So I let it sit on them, and with her blessings, I felt better at keeping it. I placed the hairpin into my pocket. 
    But now, I had more questions."
    
    show lily neutral at right 

    main ".Who are you? And why do you... Erm... Look so different than me?"

    show old lady sad at left

    granny "I do believe that I'm what could be described best as a ghost, dear."    
    
    "As she said that her smile and voice had gained a more somber tone."

    show lily shocked at right 

    main "You're a ghost?" 

    "But there was only one logical conclusion. Was I dead? But I didn't dare to voice that out."

    main "I'm so sorry heat that." 

    granny "Please lift up your head. I'm a bag of old bones by now, being a ghost is better than living through my final days. 
    Dying was easier for me, than clinging to life. I died in a bed, wihtout much trouble during midnight. Besides, death is what awaits us at the end."

    "I felt a stinging pain in my chest."

    show lily sad at right

    show old lady happy at left

    granny "But I do understand why you might not feel the same, deat. You are still so very 
    young after all. I'm sure life has many wonderful things yet to show you..."

    "The irony was that I saw nothing else to live for. And a pain deep within my own chest as though something was missing."

    show old lady shocked at left

    granny "Oh my, did I say something wrong?"

    main "It's nothing wrong."

    "I turned away from her to look at the garden again."

    main "I'm still just a bit confused about why all this is happening. I have always had that impression 
    that people just... disappear or go somewhere far, far away, when they pass. But I'm able to still see and talk to you now."

    granny "You're not wrong. Eventually it happens, and it's in an instant for some, for others it's expected by all around them. 
    I suppose this place is stuck somewhere between life and the world beyond it."

    main "I see."

    "I was in limbo or something like it."

    granny "But I think I might have an idea."

    main "What do you think it is?"

    granny "You thought you were meeting someone again. Someone dear to you here, and then you'll both depart together." 

    "I was uncomfrotable at her questioning, and wanted to direct it away. I huffed, even at her perfect little face, she knew my little secret. 
    Something that i had no intention of revealing otherwise."

    main "So, why are you still here? Why haven't you left?" 

    jump scene3

label scene3: 
    show old lady shocked at left

    granny "Ah yes, you see, I have-" 

    "Suddenly, there was a sound of something running quickly towards us. The sound of tiny paws 
    strumming intensively against the floor from somewhere inside the house."

    hide old lady shocked
    
    hide lily sad 

    show dog happy at center

    dog "YAP-YAP-YAP!"

    "I could hear a small dog barking furiously behind the door I had come through into the garden.
    I hurried to open the door and a small pomeranian jumped right at me from behind it"

    hide dog happy 

    show lily shocked at center

    main "Ack!"

    "I was barely able to dodge its fast trajectory in time.
    It landed onto a stone and instantly turned to continue yapping at me, as if trying to drive me away."

    show dog happy at left 

    show old lady neutral at right

    "I saw the ghost approach the dog. Her body lowered and bended to a sitting position so that she could pet the do."

    granny "There there, Tsuki-chan. Please, don't be so rude to our guest now."

    "As she kept talking and petting the dog, it began calming down, until it was left sternly gazing up at 
    me."

    granny "Now, could you please say hello to Lily?"

    dog "Yip!"

    "After that little bark, it turned to push its head against the lady's extended hand."

    "While watching Tsuki interacting with the ghost, I noticed that she was transparent too, just like me.
    So I assumed that her physical body had to be somewhere else as well"

    main  "Is she yours, Granny?"

    granny "She is."

    "The ghost stood up once again and began sort of walking around the garden. The dog kept 
    following her while wagging its puffy tail."
    
    granny "Although I'd rather say that she is my family."

    "The dog as her family, that must have been true, even as it reminded me that she had no one else. As I had now, no one else."

    hide lily shocked 

    "I followed after the two until they stopped near the pond. The dog jumped into the water, playing and rolling around."

    "Seeing how energetic and happy it was brought a smile to my face too."

    show old lady sad at right

    "But when I looked at the ghost again, the woman looked at her dog, with something more. Concern, perhaps, her brows furrowed together." 

    granny "I'm afraid, I haven't been quite able to leave her behind just yet. If only I knew how quickly I would have went,
    I thought I would have been able to find her a caretaker." 

    show lily sad at left 
    hide dog happy

    main "So she's the reason why you're still here."

    "I felt a lot of sympathy for the two as I watched the dog return to the woman and beg for more 
    attention and head pats from the lady, like asking the owner to cheer back up. 
    And the myth that a dog could see ghosts, was substianted right before my eyes."

    show dog happy at center

    granny "Oh Tsuki-chan... I know, I know."

    "She sat down again to pet the dog some more."

    main "Why were you waiting for me, Granny?"
    granny "Well, I suppose the passing of time does become a bit lonely at times, when you are 
    all alone here... But being able to talk to someone does make this a bit more tolerable."

    "She kept petting the dog in silence. But I know that there had to be some way to truly pass on and move on. One could not be stuck here for centuries."

    main "What would it take for you to be able to move on from this place?"

    granny "Even I do not know. I really do not want to leave my poor Tsuki behind. She 
    doesn't have anyone else to comfort her besides me now."

    "Perhaps that is why it keeps her around."

    dog "Yip!"

    hide dog happy
    
    "I was not willing to give up yet. Something about their situation, didn’t feel right to me. I wanted to do something for it. But the only thing there could change it, is me."

    main "No, there has to be something. Something that I could do to help you both..."

    "She turned her head from the dog to look at me. I could feel her gaze deep into my eyes."

    show old lady happy at right 

    granny "Then... Would you be so kind as to take care of Tsuki-chan for me?"

    show lily happy at center 

    main "Yes, of course I would!"

    "I didn't think it through, I almost did something that I regretted. But that dog and the old woman, they both touched my heart."

    granny "You promise me that... Lily?"

    main "I promise!"

    "She laughed cheerfully at my anxious response. And I wouldn't either, Tsuki didn't have anyone. I could be that someone."

    granny "Ah, don't worry, I trust you, dear. You are a very kind and loving person, I know you 
    would never abandon Tsuki."

    hide lily happy

    show dog neutral at left

    "She placed a hand on the dog's head."

    dog "Yap!"

    "The dog glanced at me and then back at the lady, while moving in place like it wasn't sure what to 
    do."

    show old lady sad at right

    show dog sad at left

    dog "Whine-whine...?"

    "The ghost stopped smiling as she stroked the dogs head. She sighed one more time"

    granny "I know,I know Tsuki. But we both know that this is for the better, right?" 

    dog "Whine..."

    "She stood up after the dog had slowly sat and lied down next to her, accepting that he would have to leave her. Such loyalty, from a dog." 

    dog "..."

    granny "Now, you promise me that you'll help and keep her company too, Tsuki-chan?"

    "The dog got back up and wagged its tail with determination."

    hide old lady 

    show lily neutral at right
    show dog happy at left

    "It then ran to jump up repeatedly, touching my leg with its front paws"

    dog "Yip-yip!"

    "After the dog's enthusiastic response, the woman smiled brightly."
    
    show old lady happy at center

    granny "Thank you so much, Tsuki-chan."

    "She then faced me"

    granny "And thank you so, so much, Lily. I will always be grateful for this."

    "She bowed in gratitude while saying that to me. And after she raised her head back up, her body 
    began to shine brightly more and more."

    show lily shocked at right

    main  "No, wait... You are leaving already? But I don't even know- Please! Wait!"

    "I tried to get closer to her, but she had already turned into a ray of light, flying up towards the sky."

    hide old lady happy

    "Only me and the dog remained in the garden..."

    main "She's gone, just like that?"

    "I collapsed onto my knees and hands, she was truly gone now."

    dog "Whine..."

    "I look at the dog, wondering what I had just gotten myself into. Or whether this was my way out, she didn't think I would follow her, so her dog would be alright."

    "It was terrifying. To be talking like that with someone and them to just disappear without a trace. I 
    hadn't been prepared for it at all, even if I thought I had been before. The last wisps and memory of her just gone like that,
    and I know it before."

    "I buried my face into my hands. I could feel Tsuki push my head lightly with her nose."

    dog "YAP!"

    main "It's alright, I'll take care of you. As I promised oba-chan. You're safe with me now."

    "The dog began suddenly tugging at my shirt as though accepting me, I looked at the dog
    perhaps thinking that she was enough." 

    "And everything went into swirling black."

    "When I regained my senses again,
    I lifted my head to see that the sun was gone and looking up.I could see the same sky I had behind 
    my bedroom window." 
    
    scene bedroom 

    play music "audio/Title Theme FULL loop.flac"

    show lily neutral 

    "I didn't know how I got here or even why. But Tsuki was all gone. I sobbed at the thought, of not keeping a promise. 
    And thinking how Tsuki will be right now." 

    "I sat down onto my bed. I hadn't known that I still had it in me to cry, but there I was; sobing at the    
    idea of not being able to keep my promise I had just made to the old lady." 

    show lily sad

    "I wiped my tears into my sleeve after calming down a little. 
    Why am I back here? But is the hairpin still with me, or is it gone just like Tsuki."

    "I couldn't come up with any other explanation, besides that the memory or Granny's dream must 
    have disappeared with her, making it impossible for me and Tsuki to stay there."

    "My heart was wrenching as I recalled how scared Tsuki had been. She must've realized what was happening way 
    before me."

    "I hugged myself tight." 

    main "She's somewhere out there, right? I can still keep my promise?"

    "I reachecd into my pocket before fishing out the hairpin that belonged to the Granny, 
    and she gave it to me as a gift."

    "It was the source of the light, but it didn't do anything 
    anymore, no matter what I did. Yet it served as proof that it all hadn't been just a dream in the end."

    main "Granny... Are you still there?"

    "The glow faded from it...In the next moment the light seemed to transition back to my windowsill"

    "I followed the light. Now, there was yet another object left there, but because of the way it was 
    shining, I failed to tell what it was."

    "I had feeling I was probably making a mistake, but I took it anyway.
    And just like before I was fully embraced by moonlight, losing my vision to it."