def most_used(string):
    mydictionary = dict()

    for item in string:
        if item not in mydictionary:
            mydictionary[item] = 1
        else:
            mydictionary[item] += 1

    mydictionary = dict(sorted(mydictionary.items(),
                        reverse=True, key=lambda item: item[1])[:10])

    return mydictionary


if __name__ == '__main__':
    mystring = r'''
    Arcane books of forbidden lore,
    00:08
    disturbing secrets in the family bloodline,
    00:11
    and terrors so unspeakable the very thought of them might drive you mad.
    00:15
    By now, these have become standard elements in many modern horror stories.
    00:19
    But they were largely popularized by a single author–
    00:23
    one whose name has become an adjective
    00:25
    for the particular type of terror he inspired.
    00:28
    Born in Providence, Rhode Island in 1890,
    00:31
    Howard Phillips Lovecraft grew up admiring the Gothic horror stories
    00:35
    written by Edgar Allan Poe and Robert Chambers.
    00:38
    But by the time he began writing in 1917,
    00:41
    World War I had cast a long shadow over the arts.
    00:45
    People had seen real horrors,
    00:47
    and were no longer frightened of fantastical folklore.
    00:50
    Lovecraft sought to invent a new kind of terror,
    00:53
    one that responded to the rapid scientific progress of his era.
    00:57
    His stories often used scientific elements to lend eerie plausibility.
    01:01
    In "The Colour out of Space,"
    01:03
    a strange meteorite falls near a farmhouse,
    01:05
    mutating the farm into a nightmarish hellscape.
    01:09
    Others incorporated scientific methodology into their form.
    01:12
    "At the Mountains of Madness" is written as a report of an Antarctic expedition
    01:17
    that unearths things better left undiscovered.
    01:20
    In others, mathematics themselves become a source of horror,
    01:23
    as impossible geometric configurations
    01:26
    wreak havoc on the minds of any who behold them.
    01:29
    Like then-recent discoveries of subatomic particles or X-rays,
    01:32
    the forces in Lovecraft’s fiction were powerful,
    01:35
    yet often invisible and indescribable.
    01:38
    Rather than recognizable monsters, graphic violence, or startling shocks,
    01:43
    the terror of “Lovecraftian” horror lies in what’s not directly portrayed–
    01:47
    but left instead to the dark depths of our imagination.
    01:51
    Lovecraft’s dozens of short stories, novellas, and poems
    01:55
    often take place in the same fictional continuity,
    01:58
    with recurring characters, locations, and mythologies.
    02:01
    At first glance,
    02:02
    they appear to be set within Lovecraft’s contemporary New England.
    02:06
    But beneath the surface of this seemingly similar reality lie dark masters,
    02:10
    for whom Earth’s inhabitants are mere playthings.
    02:13
    More like primordial forces than mere deities,
    02:16
    Lovecraft’s Great Old Ones lurk at the corners of our reality.
    02:21
    Beings such as Yog-Sothoth,
    02:22
    “who froths as primal slime in nuclear chaos
    02:25
    beyond the nethermost outposts of space and time.”
    02:28
    Or the blind, idiot god Azathoth,
    02:31
    whose destructive impulses are stalled only by
    02:33
    the “maddening beating of vile drums
    02:35
    and the thin monotonous whine of accursed flutes.”
    02:39
    These beings exist beyond our conceptions of reality,
    02:42
    their true forms as inscrutable as their motives.
    02:45
    Lovecraft’s protagonists–
    02:46
    often researchers, anthropologists, or antiquarians–
    02:50
    stumble onto hints of their existence.
    02:52
    But even these indirect glimpses are enough to drive them insane.
    02:55
    And if they survive,
    02:57
    the reader is left with no feeling of triumph, only cosmic indifference–
    03:01
    the terrible sense that we are but insignificant specks
    03:04
    at the mercy of unfathomable forces.
    03:07
    But perhaps the greatest power these creatures had
    03:09
    was their appeal to Lovecraft’s contemporaries.
    03:12
    During his lifetime,
    03:13
    Lovecraft corresponded with other writers,
    03:16
    encouraging them to employ elements and characters from his stories in their own.
    03:21
    References to Lovecraftian gods or arcane tomes
    03:24
    can be found in many stories by his pen pals,
    03:26
    such as Robert E. Howard and Robert Bloch.
    03:30
    Today, this shared universe is called the Cthulhu Mythos,
    03:33
    named after Lovecraft’s infamous blend of dragon and octopus.
    03:38
    Unfortunately,
    03:39
    Lovecraft’s fear of the unknown found a less savory expression
    03:42
    in his personal views.
    03:44
    The author held strong racist views,
    03:46
    and some of his works include crude stereotypes and slurs.
    03:49
    But the rich world he created would outlive his personal prejudices.
    03:53
    And after Lovecraft’s death,
    03:55
    the Cthulhu Mythos was adopted by a wide variety of authors,
    03:58
    often reimagining them from diverse perspectives
    04:01
    that transcend the author’s prejudices.
    04:04
    Despite his literary legacy,
    04:06
    Lovecraft was never able to find financial success.
    04:09
    He died unknown and penniless at the age of 46–
    04:13
    a victim of the universe’s cosmic indifference.
    04:16
    But his work has inspired numerous short stories, novels,
    04:19
    tabletop games, and cultural icons.
    04:21
    And as long as humans feel a sense of dread about our unknown future,
    04:25
    Lovecraftian horror will have a place in the darkest corners of our imagination.
    '''
    mystring = [item for item in mystring.split()]
    print(most_used(mystring))
