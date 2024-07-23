from django.shortcuts import render
from django.http import Http404
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
articles = {
    'held-together': {
        'picture': 'p-1.png',
        'article': 'Held Together',
        'text': '''Mitiga International Airport in Tripoli looked like something out of a Mad Max movie. The runways 
        were pockmarked, the hangars appeared abandoned, and the ghostly shell of a scorched, half-collapsed airliner 
        sat in one corner of the tarmac. I all but expected Lord Humungus to poke his masked head out of one of the 
        plane’s blasted windows. The scene was no surprise: The airport had witnessed successive sieges during the 
        years of civil war that followed the violent toppling of Libya’s longtime strongman, Muammar Qaddafi. The 
        real shock was how exactly I’d found myself landing there on a hellishly hot afternoon in May 2021.
        <p>
        Some backstory might help. I spent 25 years as a reporter and editor at The New York Times, and ten years 
        into that run, I was asked whether I might like to be a foreign correspondent in Africa. At the time, 
        I’d also wound up a single dad of two young girls. Just seeing that the dishes got done, the socks were 
        properly matched, and the hastily made bologna sandwiches made it into their lunch boxes felt like heroic 
        accomplishments. My life’s ambitions, rather jarringly, had shrunk to this: Get the girls to 18 years old 
        unharmed. So the idea of living in an armed compound in Nairobi while responsible for covering nearly a dozen 
        often troubled East African countries seemed an imprudent reach. I demurred.
        <p>
        Truth be told, I wasn’t sure 
        I had the guts for it anyway. I was not a particularly brave person. Was I also a coward of sorts? This was a 
        chastening worry that would stay with me over the decades after I turned down the chance to go to Nairobi. 
        Then, in 2021, shortly after going freelance, I fell in with Ian Urbina, an old colleague from the Times 
        who’d started the Outlaw Ocean Project, a nonprofit committed to some of the most daring reporting on the 
        planet. Piracy on the high seas; slavery on fishing ships; the secretive, illegal dumping of oil into the 
        ocean—Ian was covering all that and more. He was looking for an extra hand and said that I could start by 
        joining him on a reporting trip to Libya. I agreed to go.'''
    },
    'invisible-kid': {
        'picture': 'photo_2.jpg',
        'article': 'Invisible Kid',
        'text': '''Sometimes Adolfo felt like he was trapped at the bottom of an hourglass, the sand piling up around 
        him: Every falling grain meant another day of his life lost. Except that he wasn’t sure exactly what he was 
        missing. He’d been free in the world for only 14 years—about as long as it takes some woolly bear 
        caterpillars to become moths. What he remembered best was the small slice of Chicago’s South Side where he 
        grew up. He remembered selling drugs on street corners, and coming home to find no food in the house. He 
        remembered being evicted 11 times in 12 years, and sleeping in apartments crammed with other kids, 
        aunties and uncles, friends. He remembered doing wheelies on his bike, showing off to the other kids in his 
        neighborhood. He remembered getting up early on Sundays to get a Super Transfer—a bus ticket good for an 
        entire day—and riding downtown, where skyscrapers towered above him. He and his friends would spend the day 
        shining shoes or breakdancing for money.'''
    },
    'raised-the-children-of-america': {
        'picture': 'photo_3.jpg',
        'article': 'Raised the Children of America',
        'text': '''John Lasseter and Pixar have been helping boys grow into good men. Everything is going to be fine. 
        <p> The father is getting drunk, and so are his children. It is the end of the day, and they are celebrating. 
        The children are bringing their work to their father for his approval. When he approves, they drink. They are 
        very talented children. He is a very encouraging father. They drink often. <p> The father's name is John 
        Lasseter. Though not a particularly famous man, he is the creator of famous things. He's created the movies 
        Toy Story and Cars, for instance, whose fame among children is as everlasting as the millions of small 
        plastic products they've spawned. And he's also one of the creators of Pixar, the animation studio, 
        which means that he's created ... well, this. He's created a place where he encourages the young and the 
        talented, and where the young and the talented become his progeny. He's created a place where his approval is 
        never withheld and yet where his approval, once granted, sets off riotous celebrations. He's created a place 
        where, on a Friday afternoon, he sits in front of a monitor, in a small room at Pixar's headquarters, 
        studying the verisimilitude of cars that talk and slap each other five, while the animators who have given 
        them life line up to hear whether they've succeeded in bringing them to life. They're sitting on couches in 
        the office, and they're spilling outside the door, and when Lasseter calls their names, they take their place 
        on a leather chair in the middle of the office and wait for his judgment, with bottles of alcoholic beverages 
        in their hands. <p> It's their final day of a year spent working on the movie that Lasseter is directing for 
        release this summer — Cars 2 — and outside the little office, a party has already started. Inside, however, 
        they're all still working, when a tall young woman with limp hair and emphatic eyewear submits, 
        for Lasseter's approval, a few seconds of film in which the character of the rusty tow truck, Mater, 
        spits out the spicy food he's been eating because it's too strong for him. Lasseter approves, so she pours 
        him a shot from the bottle of Maker's 46 she has in her lap. He drinks, she drinks, and when her eyes bulge 
        and she spits it out because it's too strong for her, well, that's when the party really starts, because it's 
        the perfect Pixar moment, wherein life doesn't find its way onto the screen so much as the screen finds its 
        way into life. A few minutes later, Lasseter picks up a phone and makes an announcement over the intercom 
        that rings throughout the entire building: "This is John Lasseter. I am proud to announce that animation for 
        Cars 2 is now ... final!"'''
    },
    'president-obama-and-bill-simmons-the-gq-interview': {
        'picture': 'photo_4.jpg',
        'article': 'President Obama and Bill Simmons: The GQ Interview',
        'text': '''There's the president of the United States, and then there’s the person who happens to be the 
        President of the United States. <p> Bill Clinton served for eight years, but we were always more intrigued by 
        Bill Clinton the Person—a magnetic charmer once described by Chris Rock as “a cool guy, like the president of 
        a record company.” Clinton’s charisma defined his presidency, for better and for worse. He couldn’t always 
        harness it. He couldn’t stop trying to win everyone over, whether it was a 60 Minutes correspondent, 
        500 powerful donors in a crowded banquet hall, or a fetching woman on a rope line. <p> If Clinton acted like 
        someone who ran Capitol Records, Obama—both the person and the president—carries himself like Roger Federer, 
        a merciless competitor who keeps coming and coming, only there’s a serenity about him that disarms just about 
        everyone. At one point during the hour I spent interviewing him at the White House this fall, he casually 
        compared himself to Aaron Rodgers, and he wasn’t bragging. Obama identified with Rodgers’s ability to keep 
        his focus downfield despite all the chaos happening in front of him. That’s Obama’s enduring quality, 
        and (to borrow another sports term) this has been his “career year.” <p> Obama lives in America’s most famous 
        museum and uses it to his advantage. You’re sitting there in some ancient tearoom waiting for him to show up, 
        surrounded by portraits of former first ladies and framed maps from battles that America won over the 
        centuries. Everyone is friendly but suspicious. Everyone talks in hushed tones. You feel like you’re 
        intruding at all times. You’re just…waiting. Suddenly, ten anonymous security guards pop out of hallways and 
        doorways that you didn’t know were there. The energy shifts. And then, there’s Obama—big smile, 
        big handshake, some ball-busting comments to put everyone at ease. Within seconds of greeting me, 
        he was poking fun at my shoes and teasing me for not writing anymore.'''
    },
    'david-horowitz-is-homeless': {
        'picture': 'photo_5.jpg',
        'article': 'David Horowitz Is Homeless',
        'text': '''The first thing that David Horowitz wanted me to know was that he rarely leaves the house anymore. 
        But one evening this past January, he graciously mustered the energy to meet me at a strip-mall steakhouse 
        down the road from his home in California’s Santa Maria Valley, because he wanted to make himself clear. 
        “I’ve been ghettoized,” he said. “My wings have been clipped.” <p> Just a decade ago, a National Review 
        editor labeled Horowitz “the Most Valuable Player of the Right.” Now, sequestered on an acre and a half of 
        land with his wife and six dogs—five of them Chihuahuas—the 73-year-old ex-Communist firebrand juggles 
        writing projects while keeping his distance from all manner of political distraction. “I don’t read any 
        magazines. I hardly even read FrontPage,” he told me, though he is listed on the online right-wing journal’s 
        masthead as editor-in-chief. “I don’t read the L.A. Times or the New York Times. I despise the Times.” <p> 
        Within minutes, however, he was grumbling about an article that appeared in the Times Magazine a day before, 
        a long and sympathetic profile of the jailed former leftist zealot Judy Clark, who currently serves a 75-year 
        sentence for her role as accomplice to a 1981 armed robbery—committed in the name of something called the 
        Republic of New Afrika—that left a Brinks guard and two police officers dead. The article begins skeptically 
        but concludes that Clark has genuinely reformed. Horowitz wasn’t buying it. “What I hold against these people 
        is their unreadiness even 40 years later to tell the truth. It’s a total deception.” <p> This sense of an 
        ongoing total deception—the word “total” is the crucial descriptor–perpetrated by the American left has 
        animated Horowitz’s tireless crusade over the past four decades. A Queens-born red-diaper baby turned 
        architect of Berkeley’s New Left, he spent three decades behind enemy lines; as a result he sees himself as 
        the man best positioned to discover the opponent’s hidden agenda. As chronicled in his gripping, 
        anguished 1996 autobiography Radical Son, the seeds of his political disillusionment were planted by his 
        father’s reaction to Nikita Khrushchev’s 1956 “secret speech” detailing Stalin’s crimes; instead of prompting 
        a candid reassessment of his father’s loyalties, it merely confirmed the obstinacy of his Communist faith. 
        Moving to Berkeley for graduate school, and later serving as editor of Ramparts magazine, Horowitz hoped that 
        the New Left could advance a socialist agenda without the encumbrances of the God that failed. But David 
        would eventually loosen the grip on his own deeply rooted dogmas in response to another leftist moral 
        abdication: the support of brutal dictatorships in Cambodia, Vietnam, and elsewhere. “I thought to myself, 
        would I rather be a prisoner in the hands of LBJ or Ho Chi Minh? It’s a no-fucking-brainer.”'''
    },
}

recent_articles = {}
for item in list(articles)[-3:]:
    recent_articles[item] = articles[item]


def index(request):
    recent_blog_posts = Post.objects.all().order_by('-date_modified')[:3]
    return render(request, 'posts/index.html', context={'recent_blog_posts': recent_blog_posts})


def posts(request):
    blog_posts = Post.objects.all()
    return render(request, 'posts/posts.html', context={'articles': articles, 'blog_posts': blog_posts})


def post_old(request, article_slug):
    try:
        article = articles[article_slug]
    except KeyError:
        raise Http404
    return render(request, 'posts/post_old.html', {'article': article, 'article_slug': article_slug})


def post(request, slug):
    blog_post = get_object_or_404(Post, slug=slug)

    return render(request, 'posts/post.html', {'blog_post': blog_post, })
