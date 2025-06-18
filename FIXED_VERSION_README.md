# Playable TWR - Fixed Version

## What Was Fixed

### 1. **Shared Focus Structure**
- **Problem**: Your ideology focuses were defined as `focus = { ... }` but referenced as `shared_focus = PTWR_Democratic_Path` etc. in the tree
- **Solution**: Converted all ideology focuses to `shared_focus = { ... }` blocks in `playable_twr_ideology_shared.txt`

### 2. **Focus Tree References**
- **Problem**: The generic tree referenced non-existent shared focuses like `PTWR_Ideology_Branch`
- **Solution**: Updated `generic.txt` to only reference actually defined shared focuses

### 3. **File Organization**
- **Problem**: Multiple conflicting files with similar names
- **Solution**: 
  - Removed `playable_twr_generic_extension.txt` (old focus definitions)
  - Removed `playable_twr_generic_shared.txt` (wrong structure)
  - Kept `playable_twr_ideology_shared.txt` (correct shared focus definitions)

## Current File Structure

```
playabletwr/common/national_focus/
├── generic.txt                           # Focus tree definition
├── twr_generic_shared.txt                # TWR core shared focuses (military, industry, politics)
└── playable_twr_ideology_shared.txt      # Your ideology shared focuses
```

## How It Works

### 1. **Focus Tree Assignment**
The `generic_focus` tree is assigned to countries that should use your extended generic tree. It includes:
- **TWR Core Focuses**: Military, aviation, naval, industry, politics
- **Your Ideology Focuses**: 9 different ideology paths with sub-branches

### 2. **Ideology Paths Available**
- **Democratic Path** (y=1-2)
- **Fascist Path** (y=3-4) 
- **Communist Path** (y=5-6)
- **Monarchist Path** (y=7-8)
- **Authoritarian Path** (y=9-10)
- **Liberal Path** (y=11-12)
- **Conservative Path** (y=13-14)
- **Socialist Path** (y=15-16)
- **Radical Path** (y=17-18)

### 3. **Each Ideology Path Includes**
- **Main Path Focus**: 70-day cost, ideology popularity boost
- **Spirit Focus**: Adds ideology-specific national spirit
- **3 Sub-Branches**: Left, center, right options with different bonuses

## Important Notes

### 1. **Mod Load Order**
- Your submod must load **after** TWR
- This ensures your shared focuses are available but don't override TWR's core files

### 2. **Country Assignment**
- Only assign the `generic_focus` tree to countries that should use your extended tree
- Countries with custom TWR focus trees should keep their original trees
- Countries that should use vanilla generic should use the vanilla tree

### 3. **Icons**
- All focuses use generic ideology icons (e.g., `GFX_goal_generic_democratic_ideology`)
- These should be available in TWR or vanilla HOI4

### 4. **Ideas**
- The focuses reference ideas like `playable_twr_democratic_spirit`
- You'll need to define these ideas in your `common/ideas/` folder

## Troubleshooting

### If Focuses Don't Appear:
1. **Check Mod Load Order**: Your submod must load after TWR
2. **Clear Cache**: Delete `Documents/Paradox Interactive/Hearts of Iron IV/logs/` and restart
3. **Check Syntax**: Ensure no syntax errors in shared focus files
4. **Verify Icons**: Make sure icon names exist in TWR/vanilla

### If Focuses Overlap:
1. **Check Country Assignment**: Only assign to appropriate countries
2. **Verify Coordinates**: Each focus has unique x,y coordinates
3. **Check Prerequisites**: Ensure focus chains are properly linked

### If Tree Doesn't Load:
1. **File Location**: Ensure files are in correct folders
2. **File Names**: Check for typos in file names
3. **Syntax Errors**: Validate all focus definitions

## Next Steps

1. **Define Ideas**: Create the national spirit ideas referenced in the focuses
2. **Add Localization**: Add text for all focus names and descriptions
3. **Test Countries**: Assign the tree to test countries and verify functionality
4. **Balance**: Adjust focus costs, rewards, and effects as needed

## References

- [HOI4 National Focus Modding](https://hoi4.paradoxwikis.com/National_focus_modding)
- [Mod Load Order Guide](https://steamcommunity.com/app/394360/discussions/0/365172547938488678/) 