# ISRCFRCDB - ISRC First Registrant Code DataBase
This repository attempts to collect registrant/owner codes from ISRCs, as well as providing information about the labels/distributors that own the registrant codes.

All registrant codes are stored in the `isrc` folder. To query a registrant code with external applications, current recommended method is through jsdelivr (as it responds as application/json rather than text/plain)

Example: 
| Registrant | Code | Link |
| ----------- | ----------- | ----------- |
| Label Worx | GBQKU | https://cdn.jsdelivr.net/gh/1011025m/ISRCFRCDB/isrc/GBKQU.json |
| DistroKid | QZDA6 | https://cdn.jsdelivr.net/gh/1011025m/ISRCFRCDB/isrc/QZDA6.json |

Note that some huge distributors may have two or more registrant codes to handle the amount of releases they publish each year.

If the entry is in the repository, it will return 200. Otherwise, 404.

## Registrant code not found!
Make a PR with the title being the country & registrant code you're adding. One at a time. Use `add_entry.py` to add an entry with ease.

Be very careful and check if the registrant code belongs to a higher up distributor, an independent label or an artist. Some labels/artists don't have their own codes and rely on the distributor to do the work for them.

Some record labels may also have changed their distributor in the past. In this case, you should add the record label to all of the distributors that they have worked with as a sublabel.

If a record label uses their own ISRC registrant code rather than their distributor's, do not add the record label to the distributor as a sublabel. (unless previously released with the distributor's ISRC registrant code)

Do not add individual artists as sublabels.

Read the contribution guide (coming soon, check the example.json for now)