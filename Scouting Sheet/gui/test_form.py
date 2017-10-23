import formlayout

formdata = [('Team Number'),
            ('Match Number', 0),
            ('Alliance Color is Red (Blue if unchecked)', True),
            (None, None),
            (None, 'Autonomous'),
            ('Breaks Baseline?', True),
            (None, None),
            (None, 'Teleoperated'),
            ('Primary Scoring Location', ('Low Goal', 'High Goal', 'Neither')),
            ('Shots Fired', 0),
            ('Shots Made', 0),
            ]
formlayout.fedit(formdata, title="Red Alliance: Match Data", comment="FRC Team <b>283's</b> Red Alliance System!")