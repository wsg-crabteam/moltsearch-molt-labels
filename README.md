# Molt Search Crab Molt Image Labels
Labeled crab molt images from Molt Search submissions, to support future computer vision work--someday part of a broader effort called **CVforCrabID** (Computer vision for Crab ID: Scaling Molt Search)

> **Status:** This repository currently provides a labeled dataset only. No model development is underway. The project ideas below describe possible future directions, not committed work.

## About CVforCrabID
### Why This Project?
The Molt Search program is growing. To reach a scale most useful to natural resource managers (WDFW) & Dungeness crab researchers, it needs more reports from more places.
**Challenge:** To maintain a high quality dataset, Washington Sea Grant staff currently review and correct every report by hand. This manual review step is a bottleneck that limits program growth.
**Opportunity:** Molt Search reports follow a standardized layout, making them well suited for computer vision. A well-fit model could help staff review reports faster and more accurately.

### Project Idea
Develop a computer vision model to:
* Identify & count native Dungeness and invasive European green crabs in report images
* Flag difficult images for human review

#### Possible Next Steps
* Partner with an external collaborator (e.g. AI for Conservation community)
* Use this dataset to develop & evaluate a computer vision model (e.g. as a student capstone project or thesis work)
* Train & test a model, or launch a leaderboard to engage broader machine learning community
* If successful, integrate into data workflows (e.g. MyCoast) and participant training

## Molt Search Program basics
<a href="https://wsgcrabteam.uw.edu/programs/molt-search/">Molt Search</a> is a participatory science program based in Washington State, USA. Washington Sea Grant and Washington State University Extension teamed up in 2023 to launch a volunteer-based early detection program as a complement the existing <a href="https://wsgcrabteam.uw.edu/programs/monitoring-network/">WSG Crab Team monitoring network</a>.

Molt Search supports broader participation in early detection along inland Washington's shorelines. It engages participants in simple, standardized steps for searching for European green crab (*Carcinus maenas*) molts and reporting whether they found any via a mobile app. Molts (the outer shell of crabs left behind when they grow) can be an early sign that European green crabs have reached a new area. Data on native Dungeness crab molts is also collected from Molt Searches to add further value: Dungeness molt data helps fill a significant gap in what's known about the range and growth of juvenile Dungeness crab, whose preferred habitats overlap with the invader's.

Molt Search reports consist of a small amount of metadata (e.g. location, time, optional measurements) and an overhead photograph of all molts collected during a standardized time. Submissions are made via the <a href="https://www.mycoast.org/wa/crab">MyCoast app or website</a> and are available there once published publicly following review, currently done manually by Washington Sea Grant staff.

The Molt Search ID guide and a brief overview of protocols is available <a href="https://wsgcrabteam.uw.edu/wp-content/uploads/2026/04/25MoltSearchID3.5_LEGAL-1.pdf">here on the Molt Search website</a>. For fuller protocol nuance, contact Washington Sea Grant's Molt Search staff (see contact information below).

 
---
 
## Dataset: Molt Search crab molt image labels
 
Bounding-box labels for 452 photos from Molt Search reports. This dataset contains **labels only**. The photos stay on MyCoast and are linked by URL.
 
The model goal above focuses on Dungeness and European green crab, but every crab in each photo was labeled to species where possible. This gives a model examples of the native species it must learn to tell apart from green crab, and makes counts and "flag for review" decisions possible across the full photo. This also opens up a possible pathway for extracting additional data on crab species composition from reports in the future.

<img width="759" height="672" alt="Screenshot 2026-11-12 at 10 56 02 AM" src="https://github.com/user-attachments/assets/637077b5-0bf9-41b1-aeaa-a2304f87fa1d" />

 
### Contents
 
| File | Description |
|---|---|
| `MoltSearch_image_labels.csv` | One row per labeled image (452 rows) |
| `README.md` | This file |
 
### Summary
 
- **Images:** 452
- **MyCoast reports:** 362. Some reports include more than one photo.
- **Bounding boxes:** 10,038. A single image has between 0 and 257 boxes.
- **Images with no crabs:** 7
- **Photo dates:** April 2023 – August 2025
- **Location:** Washington State shorelines
- **Labeler:** Lisa Watkins, Washington Sea Grant
- **Labeling dates:** September 2025 and November 2026
### File format
 
`MoltSearch_image_labels.csv` has three columns:
 
| Column | Description |
|---|---|
| `ID#` | MyCoast report ID. The full report is at `https://mycoast.org/reports/<ID#>`. When a report has several photos, its ID appears on several rows. |
| `image_URL` | Direct link to the photo on the MyCoast image server. |
| `annotations` | A list of bounding boxes for that image, stored as JSON. An empty list (`[]`) means the image was reviewed and had no crabs in it. |
 
Each bounding box looks like this:
 
```json
{"label": "Dungeness crab", "x": 91, "y": 911, "width": 506, "height": 430}
```
 
- All values are in **pixels of the full-resolution image**.
- `x` and `y` are the **top-left corner** of the box. `width` and `height` extend right and down from that corner.
- Values are rounded to whole pixels.
#### Be sure to rotate images before using the boxes
 
The boxes were drawn in a web browser. Browsers use each photo's EXIF orientation tag to turn it upright before displaying it, so the boxes match the **upright** photo. Phone photos are often stored sideways with a tag saying how to rotate them. If you load an image without applying that tag, the boxes will be in the wrong place.
 
### Labels
 
| Label | Boxes | Images containing it |
|---|---:|---:|
| Hairy shore crab | 3,288 | 203 |
| Purple shore crab | 2,072 | 204 |
| Dungeness crab | 1,493 | 222 |
| Crab, uncertain ID | 1,385 | 140 |
| Red rock crab | 1,075 | 222 |
| Graceful crab | 436 | 117 |
| Hairy helmet crab | 181 | 79 |
| Spider/Kelp crab | 73 | 52 |
| European green crab | 16 | 15 |
| Pygmy Rock crab | 8 | 8 |
| Pea crab | 8 | 4 |
| Black clawed crab | 3 | 3 |
 
- **"Crab, uncertain ID"** marks a crab molt that couldn't be identified to species from the photo, for example because it was too small, blurry, broken, poorly oriented, or hidden. All upside down crab molts were given this label, as well.
- The labeling tool also offered **"Lined Shore crab"** and **"Crab, not listed"**, but neither was used.
- Labels identify crab molts. Objects in these photos are assumed to be molts, not live crabs, given the standardized protocols followed by Molt Search participants during collection.
- Species are very unevenly represented: European green crab has only 16 boxes. Any model trained on this data will need to account for that imbalance.
### How the images were selected and labeled
 
1. **Sampling.** In September 2025, 500 reports were randomly sampled (R, `set.seed(42)`, `dplyr::sample_n`) from all Molt Search reports with at least one photo in a MyCoast export dated 2025-09-01 (containing all reports that had been both submitted and manually reviewed & published by that date).
2. **Download.** Every photo from the 500 sampled reports was downloaded and named by report ID. When a report had more than one photo, the first was named `<ID#>.jpg` and the others `<ID#>_b.jpg`, `<ID#>_c.jpg`, and so on, in the order MyCoast lists them.
3. **Batching.** The downloaded photos were shuffled (`set.seed(123)`) and split into batches of up to 50 for labeling, so photos from the same report often landed in different batches.
4. **Download losses.** Some downloads failed partway through the run, most likely because the internet connection dropped. As a result, batches 8–13 held only 13–25 photos each instead of 50. The failures depended on download order, not on photo content, and the photos had already been shuffled. So the labeled set should still be an unbiased subset of photos from the sampled reports.
5. **Labeling.** One person (the author, former Molt Search program lead) drew a box around every visible crab or crab molt in each photo and assigned it a label, using a custom browser-based tool. Each photo was labeled once, and no second labeler checked the work. All 13 batches were labeled, for a total of **452 photos from 362 of the 500 sampled reports**. For 34 of those reports, only some of their photos were labeled (due to incomplete download). The other 138 sampled reports have no labeled photos (due to incomplete download).
### Notes for using this dataset
 
- **Split training and test sets by report.** Photos from the same report often show the same molts from different angles. Put all photos with the same `ID#` in the same split, or test results will look better than they really are.
- **Volunteer photos vary widely.** Each report's main photo is meant to be an overhead shot of all molts collected during the timed search with an object for scale, but lighting, distance, background, arrangement, and how closely volunteers followed the layout all vary. Extra photos in a report (`_b`, `_c`, ...) may be close-ups or other angles.
- **Image links may change.** The URLs point to MyCoast's servers, and this dataset can't guarantee they'll stay available.
- **More information about each report** (date, location, what the volunteer recorded) is in the MyCoast data. Join it to this file on `ID#`. [TODO: link to the Molt Search dataset repository/DOI once published.]
## License
 
The labels in `MoltSearch_image_labels.csv` are released under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
 
**This license covers the labels only, not the photos.** The linked photos were taken by Molt Search participants and submitted through MyCoast. Their use is governed by MyCoast's terms, not this license.
 
## Suggested citation
 
> Watkins, L. (2026). *Molt Search Crab Molt Image Labels* (Version 1.0) [Data set]. Washington Sea Grant. 
 
## Acknowledgments
 
The photos in this dataset were taken and submitted by Molt Search participants, whose time and care made this work possible. Molt Search is a program of Washington Sea Grant in partnership with Washington State University Extension. MyCoast hosts the reports and images.
 
## Contact
 
Washington Sea Grant Crab Team staff, who lead the Molt Search program: crabteam@uw.edu
