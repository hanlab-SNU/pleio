# PLEIO 
- Pleiotropic Locus Exploration and Interpretation using Optimal test

`pleio` is a command line tool for performinig meta-analysis of multiple GWAS summary statistics. 

## Getting Started

In order to download `pleio`, you should clone this repository via the command
```
git clone git://github.com/hanlab-SNU/pleio.git
cd pleio
```

In order to run `pleio`, the following python dependencies must be installed in your system.

- python >= 3.7.4
- pandas >= 1.0.4
- numpy >= v.1.18.1
- scipy >= v.1.4.1

Once the above has completed, you can run the following command:

```
./pleio -h
```

## Updating PLEIO
You can update to the newest version of `PLEIO` using git. First, navigate to your pleio/ directory (e.g., cd pleio), then run
```
git pull
```
If `PLEIO` is up to date, you will see
```
Already up-to-date.
```
otherwise, you will see `git` output similar to 
```
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 6 (delta 4), reused 5 (delta 3), pack-reused 0
Unpacking objects: 100% (6/6), done.
From git://github.com/hanlab-SNU/pleio
   e065a06..14c3399  master     -> origin/master
Updating e065a06..14c3399
Fast-forward
 README.md       | 2 +-
 ldsc_preprocess | 2 +-
 2 files changed, 2 insertions(+), 2 deletions(-)
```

## Tutorial 
If you want to try a joint analysis of 18 characteristics of cardiovascular diseases using the PLEIO framework, please use the following [link](https://github.com/hanlab-SNU/pleio/wiki/Identification-of-pleiotropic-loci-with-PLEIO)

## Citation

If you use the software, please cite  
Cue Hyunkyu Lee., Huwenbo Shi., Bogdan Pasaniuc., Eleazar Eskin., Buhm Han. A method to map and interpret pleiotropic loci using summary statistics of multiple traits. bioRxiv 2020.06.16.155879; doi: https://doi.org/10.1101/2020.06.16.155879

## Support

Issues with PLEIO? Email cuelee@snu.ac.kr

## License 

This project has no license currently.

## Authors

Cue Hyunkyu Lee ( Seoul National University )
