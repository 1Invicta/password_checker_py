# [ updates.py ] #


# ======== Setup ======== #

repo_link = "https://github.com/1Invicta/password_checker_py"

changelog = [
    {
        # First public build
        "date": "28/09/2025",
        "version": "0.1.0",
        "changes": [
            ("added", "Created main password checking framework system"),
            ("added", "Added menus and terminal user interface"),
            ("fix", "Fixed various menu and user interface bugs"),
            ("removed", "Removed redundant code for optimization")
        ]
    },
    {
        # Minor fixes (menus, optimization)
        "date": "06/10/25",
        "version": "0.1.1",
        "changes": [
            ("fix", "Improved menus"),
            ("fix", "Optimized code")
        ]
    },
    {
        # More fixes and optimization
        "date": "07/10/25",
        "version": "0.1.2",
        "changes": [
            ("fix", "Fixed bugs"),
            ("fix", "Optimized menu system")
        ]
    },
    {
        # Structural improvement (modularization)
        "date": "09/10/25",
        "version": "0.1.3",
        "changes": [
            ("fix", "Split scripts for modularization and readability")
        ]
    },
    {
        # New release - GitHub uploadd & reorganization
        "date": "23/10/25",
        "version": "0.2.0",
        "changes": [
            ("added", "Uploaded tool to GitHub! (Check 'info' menu for the link)"),
            ("fix", "Reorganized scripts for improved readability"),
            ("removed", "Removed redundant code, variables and arguments")
        ]
    },
    {
        # Helper scripts and improved menus
        "date": "27/10/25",
        "version": "0.2.1",
        "changes": [
            ("added", "Added 'utils.py' script for helper functions"),
            ("added", "Added better comments for organization and readability"),
            ("fix", "Tweaked and improved menu system"),
            ("fix", "Automated up repetitive code and debugging")
        ]
    },
    {
        # Major new feature: password check modes
        "date": "28/10/25",
        "version": "0.3.0",
        "changes": [
            ("added", "Added password check modes! ('Default', 'Advanced', 'Extreme')"),
            ("added", "Improved password check and rating system"),
            ("added", "Implemented better error handling everywhere"),
            ("fix", "Fixed buggy 'utils.py' functions"),
            ("fix", "Fixed main menu bug: couldn't input '0' as valid menu"),
            ("fix", "Replaced redudant code with 'utils.py' helper functions"),
            ("fix", "Fixed various bugs"),
            ("removed", "Removed confusing comments")
        ]
    },
    {
        # Major fixes + testing => NO BUGS FOUND!
        "date": "29/10/2025",
        "version": "0.3.1",
        "changes": [
            ("added", "Created 'updates.py' file to store past update logs"),
            ("added", "Added structured and consistent comments everywhere"),
            ("fix", "Refactored lengthy functions to improve readability and performance"),
            ("fix", "Fixed path-related bug in 'utils' module"),
            ("fix", "Fixed various argument-handling issues in menu functions"),
            ("fix", "Renamed several functions for better clarity and consistency"),
            ("removed", "Removed the large, redundant 'updates' list from a function (finally)")
        ]
    },
    {
        # Added/Fixed function comments
        "date": "30/10/2025",
        "version": "0.3.2",
        "changes": [
            ("added", "Added missing function comments and fixed existing ones"),
            ("added", "Implemented various quality-of-life improvements"),
            ("fix", "Replaced manual print statements with utility functions"),
            ("fix", "Reordered functions for better readability"),
            ("removed", "Removed redundant comments")
        ]
    },
    {
        # Normalized rating results
        "date": "31/10/2025",
        "version": "0.3.3",
        "changes":
        [
            ("fix", "Improved wordlist check performance"),
            ("fix", "Improved consistency in password check results")
        ]
    },
    {
        # Worked on password checks
        "date": "02/11/2025",
        "version": "0.3.4",
        "changes":
        [
            ("added", "Added entropy validation for enhanced reliability"),
            ("fix", "Rating system adjustments and optimized performance checks"),
            ("fix", "Improved stability with enhanced error handling"),
            ("fix", "Profiled password checks and greatly improved performance")
        ]
    },
    {
        # Pattern checking added
        "date": "05/11/2025",
        "version": "0.3.5",
        "changes":
        [
            ("added", "Implemented pattern checking in password checks"),
            ("fix", "Improved type hinting and comments for readability"),
            ("fix", "Extracted global constants and variables as modules"),
            ("fix", "Reorganized scripts and directories for a better project structure"),
            ("removed", "Demolished password rating inconsistencies! (finally...)")
        ]
    },
    {
        # performance patch
        "date": "06/11/2025",
        "version": "0.3.6",
        "changes":
        [
            ("fix", "Replaced wildcard imports with explicit imports"),
            ("fix", "Fixed nested f-strings")
        ]
    },
    {
        # generator menu
        "date": "15/11/2025",
        "version": "0.3.7",
        "changes":
        [
            ("added", "Added password generator menu"),
            ("added", "Added output result functionality in JSON format"),
            ("fix", "Packaged project for distribution"),
            ("fix", "Corrected module imports and resolved inconsistencies \n\twith argument handling and nested f-string return values"),
            ("fix", "Adjusted password check mode requirements")
        ]
    },
    {
        # hotfixes patch
        "date": "15/01/2026",
        "version": "0.3.8",
        "changes":
        [
            ("fix", "Fixed password check feedback bugs"),
            ("fix", "Improved user interface for argument results")
        ]
    },
    {
        # linux support fixing f-strings
        "date": "19/01/2026",
        "version": "0.3.9",
        "changes":
        [
            ("fix", "Fixed feedback message errors"),
            ("fix", "Removed more nested f-strings")
        ]
    }
]