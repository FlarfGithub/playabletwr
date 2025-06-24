# Playable TWR Submod

A comprehensive submod for the Thousand Week Reich (TWR) mod that adds nine new generic ideology focus branches, political advisors, and enhanced gameplay mechanics for generic countries.

## Features

### 🎯 Nine Ideology Focus Branches
- **Fascist Path**: Iron fist rule with propaganda and mobilization
- **Communist Path**: Revolutionary change and worker mobilization  
- **Monarchist Path**: Royal restoration and traditional values
- **Democratic Path**: Liberal democracy and constitutional reform
- **Authoritarian Path**: Military rule and strong leadership
- **Liberal Path**: Progressive reforms and civil liberties
- **Conservative Path**: Traditional governance and stability
- **Socialist Path**: Worker empowerment and social reform
- **Technocrat Path**: Expert-led governance and efficiency

### 👥 Political Advisors
Each ideology includes three tiers of political advisors with unique bonuses and modifiers, providing strategic depth to political management.

### 🎮 Enhanced Gameplay
- **Dynamic Ideology Drift**: Political changes based on garrison control and events
- **Event Chains**: Rich narrative events for each ideology path
- **Spirit System**: Temporary and permanent national spirits for each ideology
- **AI Integration**: AI-controlled generic countries use the new ideology system

## Installation

### Prerequisites
- Hearts of Iron IV (latest version)
- Thousand Week Reich mod (Steam Workshop ID: 2204739234)

### Manual Installation
1. Download or clone this repository
2. Place the `playabletwr` folder in your HOI4 mods directory:
   ```
   Documents/Paradox Interactive/Hearts of Iron IV/mod/
   ```
3. Enable the mod in the HOI4 launcher
4. Ensure TWR mod is enabled and loaded before this submod

### Steam Workshop (Coming Soon)
The mod will be available on Steam Workshop for easy installation.

## Game Rules

The mod includes several game rules to customize your experience:

- **Generic Ideology Focuses**: Enable/disable the new focus trees
- **Generic Ideology Advisors**: Enable/disable the new political advisors  
- **Generic Ideology AI**: Control AI behavior with the new system

## Troubleshooting

### Common Issues

#### Game Crashes on Launch
- Ensure TWR mod is enabled and up to date
- Clear HOI4 mod cache in Steam
- Verify game files integrity
- Check that all required DLCs are installed

#### Focus Trees Not Appearing
- Verify the mod is properly installed in the correct directory
- Check that TWR mod is loaded before this submod
- Ensure game rules are set to enable generic ideology focuses

#### Missing Localization
- Clear HOI4 cache and restart
- Verify all localization files are present
- Check for syntax errors in localization files

#### Ideology Changes Not Working
- Ensure you're playing as a generic country
- Check that the appropriate game rules are enabled
- Verify focus tree completion and event triggers

### Error Logs
If you encounter issues, check the HOI4 error logs located at:
```
Documents/Paradox Interactive/Hearts of Iron IV/logs/
```

## Development

### File Structure
```
playabletwr/
├── common/
│   ├── national_focus/
│   │   ├── playabletwr_ideology_shared.txt    # Main ideology focus trees
│   │   └── generic.txt                        # Generic focus tree integration
│   ├── ideas/
│   │   ├── TWR_ideology_spirits.txt          # National spirits
│   │   └── TWR_ideology_advisors.txt         # Political advisors
│   └── game_rules/
│       └── 00_game_rules.txt                 # Game rule definitions
├── events/
│   └── TWR_ideology_events.txt               # Ideology-specific events
├── localisation/
│   └── english/
│       ├── playable_twr_ideology_l_english.yml
│       ├── TWR_ideology_events_l_english.yml
│       └── TWR_game_rules_l_english.yml
└── descriptor.mod                            # Mod descriptor file
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Building from Source
1. Clone the repository
2. Make your modifications
3. Test in-game
4. Commit and push changes

## Testing

This repository includes a script to check that country tags are unique in
`common/countries/colors.txt`. Run the script with Python:

```bash
python3 tests/test_unique_colors.py
```

The command exits with a non-zero status if any tag is defined more than once.

## Version History

### v1.0.0 (Current)
- Initial release with nine ideology branches
- Complete political advisor system
- Event chains for all ideologies
- Game rules integration
- Full localization support

## Credits

- **Original TWR Mod Team**: For the excellent base mod
- **Paradox Interactive**: For Hearts of Iron IV
- **Community Contributors**: For feedback and testing

## License

This mod is released under the same license as the TWR mod. Please respect the original mod's terms and conditions.

## Support

For issues, questions, or suggestions:
- Create an issue on GitHub
- Join our Discord server (link coming soon)
- Check the Steam Workshop page (coming soon)

---

**Note**: This is a submod and requires the Thousand Week Reich mod to function. Always ensure TWR is up to date and properly installed. 