New semester TODO list
======================

Facebook
--------

* Create a Facebook group, name `Cloyne SEASON 'XX`, where `SEASON` is one of `Fall`, `Spring`, `Summer`, and
`XX` is year, like `Cloyne Summer '15`.
* Choose closed group within Berkeley.
* Share it on previous semester Facebook group so that people can join. Invite those you know their Facbook account.
* Allow joining only to members who live that semester in Cloyne.

Examples of past Facebook groups: [Cloyne Summer '15](https://www.facebook.com/groups/1479825148929634/),
[Cloyne Spring '15](https://www.facebook.com/groups/765891660172376/),
[Cloyne Fall '14](https://www.facebook.com/groups/628905887204288/)

Mailing lists
-------------

For mailing list we use [Sympa](http://sympa.org/) installed at [http://cloyne.org/lists/](http://cloyne.org/lists/).
Tasks at the beginning of the semester are:
* Remove old members from `announce@cloyne.org` mailing list and add current members.
* Rename current `clones@cloyne.org` mailing list to `clones.XXX@cloyne.org` mailing list, where `XXX` consist of a
year and season, like `clones.2014f@cloyne.org`, `clones.2015s@cloyne.org` or `clones.2015su@cloyne.org` (for summer).
* Create new `clones@cloyne.org` mailing list and add current members.
* Update `alumni@cloyne.org` mailing list to include the new `clones.XXX@cloyne.org` mailing list as data source.

Detailed steps:
* Prepare a list of current members e-mail addresses in the format `EMAIL NAME` with each entry in the separate line.
So e-mail address is separated from name with a space, and each e-mail address is in its own line. A bit of copy-pasting
and regular expressions can help you with that.
* Login with `clonm@bsc.coop` account [http://cloyne.org/lists/](http://cloyne.org/lists/).
* Open [http://cloyne.org/lists/review/announce](http://cloyne.org/lists/review/announce).
* Remove all subscribers by clicking on "Toggle selection" at the end of the page to select all, check "Quiet",
and then click on "Delete selected email addresses".
* Open [http://cloyne.org/lists/add_request/announce](http://cloyne.org/lists/add_request/announce).
* Paste in all addresses, check "Quiet", and click on "Add subscribers".
* Open [http://cloyne.org/lists/admin/clones](http://cloyne.org/lists/admin/clones).
* Click "Rename list" and the new `clones.XXX@cloyne.org` name.
* Open [http://cloyne.org/lists/create_list_request](http://cloyne.org/lists/create_list_request).
* Choose to copy `clones.XXX@cloyne.org` mailing list as `clones@cloyne.org`. We are preparing now the new mailing
list. This copies the configuration, but not subscribers.
* Open [http://cloyne.org/lists/add_request/clones](http://cloyne.org/lists/add_request/clones).
* Paste in all addresses, check "Quiet", and click on "Add subscribers".
* Open the "List definition" admin page of the new `clones.XXX@cloyne.org` mailing list, for example for
`clones.2015s@cloyne.org` open `http://cloyne.org/lists/edit_list_request/clones.2015s/description`.
* Change subject "Cloyne discussion mailing list" (which is subject for `clones@cloyne.org` mailing list) to
`Cloyne YEAR SEASON discussion mailing list`, like `Cloyne 2015 spring discussion mailing list`. Click "Update" at the
end of the page.
* Open [http://cloyne.org/lists/edit_list_request/alumni/data_source](http://cloyne.org/lists/edit_list_request/alumni/data_source).
* Add to "List inclusion" the new `clones.XXX` mailing list inclusion. For example, `clones.2015s`.
Click "Update" at the end of the page.

`from-central` mailing list is automatically updated based on the subscribers from `announce` mailing list.

Wordpress
---------

* [Using this script](https://github.com/cloyne/docker-blog/blob/master/users-csv.py) you can create a CSV file from a list of e-mail addresses and names, the same as used for mailing lists. ```./users-csv.py < list > out.csv```
* All users in the CSV file will be created with `author` permission which allows them to post blog posts, events,
upload media content, but does not allow them to change content of others.
* Open [http://cloyne.org/wp-admin/users.php?page=import-users-from-csv](http://cloyne.org/wp-admin/users.php?page=import-users-from-csv).
* Select the CSV file, check "Send to new users" and "Show password nag on new users signon ". Click "Import".

It might happen that the site time-outs after the import. This is normal. New users will be imported and e-mail
notification will be send to them inviting them to set the password.

Notifying members
-----------------

After all of the above was done, you should send a message to members informing them what is available to them and
how to use it.

The `announce@cloyne.org` e-mail template:

```
Welcome to Cloyne from your network manager. I configured our mailing
lists for the new period. For those who are new to Cloyne, here are few
instructions on how to navigate the digital Cloynosphere.

We have three main mailing lists to which you are all subscribed initially:

announce@cloyne.org - to which managers will be sending important
information to all of us, any discussion direct to:

clones@cloyne.org - discussion mailing list for all of us to keep
virtual flow of information going, any discussion goes, but remember
that the whole house is subscribed to this mailing list (if needed,
feel free to request a dedicated mailing list for your project, group,
team, interests, etc., so that members can subscribe to those they are
interested in)

from-central@cloyne.org - similar to announce, just that for information
from the central level we are forwarding to the house

If you want to change the e-mail address you are subscribed to mailing
lists with, talk to Graham.

We have a website (http://cloyne.org/). And we have also a calendar
of events on the website. All of you should receive an e-mail
with your username and temporary password for the website. With it
you can login to the website:

http://cloyne.org/wp-login.php

You can add blog posts, add events to the calendar, and upload
photos and videos to our media library. The site is yours. Enjoy it.

If you prefer Facebook, we also have a Facebook group:

https://www.facebook.com/groups/1479825148929634/

If anyone is interested in helping doing computer, network, and similar
stuff, tell me and let's hack together. :-)
```

The `clones.XXX@cloyne.org` e-mail template:

```
The clones@cloyne.org mailing list has been renamed to
clones.XXX@cloyne.org with all the members from YEAR OLD_SEASON kept there.

The new clones@cloyne.org mailing list has only the NEW_SEASON members on it.

There is also a alumni@cloyne.org mailing list, which is a superset of
all clones.*@cloyne.org mailing lists, so all past members of Cloyne.

Feel free to use them. Feel free to unsubscribe. Feel free to change the
e-mail address with which you are subscribed to one which will last
(not @berkeley address).

http://cloyne.org/lists/
```

What is hackerspace:

```
What hackerspace is. In short, it is a space where you can work on your
projects, be creative. Hacking here means in some way taking things
apart, learning how they work, building things from other stuff, often
stuff which had originally some other purpose. And it does not have to
be at all related to computer science, you can hack law, philosophy,
clothes, privilege.

So, no, hackers do *not* look like that:

http://www.sadanduseless.com/2011/12/stock-photo-hackers/

I think you should all see this great talk by Mitch about what
hackerspaces are above:

https://www.youtube.com/watch?v=WkiX7R1-kaY

Mitch was also at Cloyne, having a soldering workshop:

http://cloyne.org/events/soldering-workshop/

Look at us:

http://cloyne.org/2014/09/report-soldering-with-mitch-altman/

So, space is for you and your creativity!
```

Instructions
============

Later on you should send few e-mails with various instructions.

`Adding events to your Google Calendar` template:

```
If you want, you can add events from cloyne.org website to your Google
Calendar. On events page you have iCal link:

http://cloyne.org/events/

Copy the URL and add it to your Google Calendar as described for you
on the following page under the section "Example: Subscribing to
Events Using Google Calendar":

http://wp-events-plugin.com/documentation/event-ical-feeds/
```

`How to use Gmail for mailing lists` template:

```
Do you feel overwhelmed with all the e-mails coming your way over our
mailing lists? Are you using Gmail? Worry not, there are some easy
tricks to empower you and get you in charge of which discussions you
want to read and which to ignore.

There are two ways of dealing with mailing list:
- you can label and filter them
- or you can mute individual conversations you don't want to appear in
your inbox anymore

You can get the whole mailing list be filtered under one label. instructions:

http://googlesystem.blogspot.com/2007/11/filter-messages-from-mailing-list-in.html

Gmail has support for muting one conversation:

https://support.google.com/mail/answer/47787?hl=en

You mute it once (when you discover that topic does not interest you)
and this is it.

"When you mute a conversation, new messages added to the conversation
bypass your inbox so that the conversation stays archived."

I propose the following settings:
- for announce mailing list, create a label and filter it under that
e-mail, but leave e-mails to come to you inbox
- for clones and other mailing lists, or:
  - use mute feature to mute conversations you are not interested in, or
  - you create a label and filter for it and set that it skips the
inbox and is automatically archived

If you have any questions about any of this, feel free to ask.
```

`Everyone can post to our blog and create events` template:

```
Short reminder that if anyone would like to post to a blog at
cloyne.org or create an event, you can do that! You should all
receive username you can use to login into the site. If not,
register here:

http://cloyne.org/wp-login.php?action=register

And then send me an e-mail that I give you permissions. After that,
you can make blog posts and events through admin interface:

http://cloyne.org/wp-admin/

For now, we do not have any rules what blog posts are OK, and I like
that, so let's try for now like that. If anyone feels that anything
published is objectionable, feel empowered to bring it up to or author
or managers.

Otherwise, I would really encourage all of you to take it for your own
media. Post blog posts of what you are doing, what you are proud of,
what interesting happened, anything you would like to share with house
and visitors of our website. Make it fun, sad, serious, [insert your
favorite adjective], make it yours.

Create events. By creating an event, you inform the rest of the house
that something is happening, and you also clearly show that the space
will be in use.
```

`Scanning and printing` template:

```
We have a house scanner and printer. Printing operates on karma box
principle, 5 cents per page. When printing, please throw that amount
into the karma box next to the printer.

Scanning is easy, you can scan it to the USB flash drive, or send
the scanned document to your e-mail address.

For printing, you have multiple ways you can print. The easiest is to
configure it on your computer as a network printer.

Open the printer configuration on your computer and it will probably
find this printer; otherwise, you can add it with the following
information:
- name: [Library] HP LaserJet 500 MFP M525
- type: HP LaserJet 500 MFP M525
- IP Address: 10.20.32.90
- address: printer1.cloyne.net

When prompted, do not select "share printer".

To install for Windows 7, you should search on Goggle for "HP Universal
Print Driver for Windows PCL6" and install it for your system (first
hit is the right one), and then you will get that screen you have on
instructions. Windows 8 people don’t have to install anything, it should
just work.

Alternativelly, you can plug your USB flash drive from the front.

You can e-mail the document you want to print to:

elvi834egmi34@hpeprint.com

But this will waste one sheet of paper per document, and will not print
double two-sided.

You can as well print from:

https://printer1.cloyne.net/hp/device/Print/Index

And remember, always print *two-sided to save paper*! Or even multiple
pages on one page. You configure that on your computer when you are
printing.

When you are printing and you are selecting trays manually, don't use
Tray 1. Tray 1 is the one where you have to manually feed the paper.
So it will not print until you give the printer the paper. But even
more importantly: if you open Tray 1, remember to close it. If it is
open, it will require paper there for anyone else who will want to
print, and nobody else will be able to print.

The printer is sometimes paused. Do not do that. If you pause the
printer, nobody else can print. There will be a small message on
the printer that it is paused and you unpause it by pressing a
small circular arrow button on the top left on the screen.
So: do not pause the printer.
```

`Scanning and printing` template in Chinese:

```
打印的方法

  打印是5分钱／一页纸。请将费用放入打印机旁边的[karma box］中。除了拿usb到打印机打印之外，你还可以通过wifi连接打印机。如果你在设置中找不到 [Library] HP LaserJet 500 MFP M525，你可以设置加入这个打印机：
- name: [Library] HP LaserJet 500 MFP M525
- type: HP LaserJet 500 MFP M525
- IP Address: 10.20.32.90
- address: printer1.cloyne.net <http://printer1.cloyne.net/>

  请记得双面打印，节约用纸：）还有为了能让大家都能打印，不要暂停打印机。

  同样的机器还可以扫描，你可以将扫描完成的文件发到自己的邮箱。
```
