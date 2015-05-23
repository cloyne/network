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

We have two main mailing lists to which you are all subscribed initially:

announce@cloyne.org - to which managers will be sending important
information to all of us, any discussion direct to:

clones@cloyne.org - discussion mailing list for all of us to keep
virtual flow of information going, any discussion goes, but remember
that the whole house is subscribed to this mailing list (if needed,
feel free to request a dedicated mailing list for your project, group,
team, interests, etc., so that members can subscribe to those they are
interested in)

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

`Printing` template:

```
For printing, you can plug your USB flash drive from front.
And you can use it both for printing from or scanning to.

When you are printing and you are selecting trays manually, don't use
Tray 1. Tray 1 is the one where you have to manually feed the paper.
So it will not print until you give the printer the paper. But even
more importantly: if you open Tray 1, remember to close it. If it is
open, it will require paper there for anyone else who will want to
print, and nobody else will be able to print.

The printer is sometimes paused. I do not know who is pressing "pause",
but if you pause the printer, nobody else can print. There will be a
small message on the printer that it is paused and you unpause it by
pressing a small circular arrow button on the top left on the screen.
So: don't pause the printer.

Please remember: always print two-sided (or even multiple pages on
one side). You configure that on your computer when you are printing.
```
