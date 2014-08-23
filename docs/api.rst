INFOPORTO COMMUNITY - API
=========================

Methods to fetch data
---------------------


``get_news``
____________

Get all news from the portal and bring them back to user in a JSON list like below: ::

    [
        {"text": "Lorem ipsum",
            "title": "dolor sit amet",
            "uid": "22cf54a562604612b07c953383a2cdfc",
            "modification_date": "06-08-2014 08:18:17",
            "description": "lorem ipsum dolor sit amet",
            "likes": 12},
        {"text": "&lt;p&gt;Lorem ipsum dolor sit amet &lt;br /&gt;",
            "title": "Lorem ipsum dolor sit amet",
            "uid": "df183a7ee7f245c2af8ad353f1ac0540",
            "modification_date": "06-08-2014 08:20:15",
            "description": "test description",
            "likes": 98}
    ]

Content of the field ``text`` is a rich text encoded.


``get_agreements``
__________________

Get all agreements object from the portal and bring them back to user in a JSON list like below: ::

    [{
        "contact_email": "sdf",
        "contact_name": "asdf",
        "contact_phone": "sdf",
        "description": "lorem ipsum",
        "end": "31-12-2014 00:00:00",
        "modification_date": "22-08-2014 10:53:48",
        "start": "01-01-2014 00:00:00",
        "title": "Convenzione di prova",
        "uid": "584dec6f385e459fbec4891a4e42ce61",
        "likes": 21
    }]


``get_events``
_____________

Get all events object from the portal and bring them back to user in a JSON list like below: ::

    [{
        "contact_email": "none@none.com",
        "contact_name": "Pablo Red",
        "contact_phone": "+39110011234",
        "description": "Lorem ipsum dolor sit amet",
        "end_date": "29-08-2014 23:25:00",
        "event_url": "http://www.example.com",
        "modification_date": "06-08-2014 08:25:28",
        "start_date": "22-08-2014 20:25:00",
        "title": "ESTATE NOVA",
        "uid": "aa8ada81f3dc467bbbb2490d93b68a53",
        "likes": 43
    }]


Methods to set data
-------------------

``set_use_agreements``
______________________

Used to send to the system the informations about a user that make a request to use an agreement.

You have to pass some data in a JSON POST: ::

    {
        "agreement_id": str
        "user_id": str
    }

It should return a JSON message like ::

    {
        "response": "Informations saved."
    }


``send_im``
___________

Used to send Instant Message across the platform. You must provide a JSON POST like below: ::

    {
        "from_id": str - (ie: admin),
        "to_id": str - static for now: admin
        "subject": str,
        "message": text
    }

It should return a JSON message like ::

    {
        "response": "Informations saved."
    }


``get_inbox``
_____________

Used to fetch al message for the current logged user. It provides a list of JSON object like below: ::

    [
        {
            "from_id": str - (ie: admin),
            "to_id": str - static for now: admin
            "subject": str,
            "message": text,
            "created_at": datetime as str,
            "status": str [options: "new, archived, deleted"]
        }
    ]


``like_it``
___________

This method is used to express a "like" for a portal object. You have to provide a JSON POST like below: ::

    {
        "user_id": str,
        "uid": str,
    }

It should return a JSON message like ::

    {
        "response": "Informations saved."
    }

Note that a second post with the same data will act as and undo of the first like.
