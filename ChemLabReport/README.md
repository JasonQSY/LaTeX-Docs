# Vc211 Chemistry Lab Report Template

The template is created by myself in my Vc211 general chemistry lab class of UM-SJTU JI. It seems the template is complicated with multiple files. However, it is proved that muiti-file system is helpful. It saves me a lot of time.

## Structure

`report.tex` is the central file of the document. It inputs other files by LaTeX `\input`. Other files follow a linear structure.

- `std-head.tex`
    - Add useful packages including `mhchem` and `amsmath`
    - I added `xeCJK` since I was required to type my Chinese name.
- `titlepage.tex`
    － Just the cover. With `\begin{titlepage}`
- `toc.tex`
    - Abbr. of table of contents.
- `background.tex`
    － Everything before PLE, e.g. objectives, introduction, background, thesis.
    - It is a separate file because I am required to complete it before the lab.
- `handwrite.tex`
    - Replace it with the handwritten procedures and PLE.
- `alr.tex`
    - Abbr. of after-lab report. It includes results, discussions, conclusions and so on.
    - It is a separate file because I am required to complete it after the lab.
- `appendix.tex`
    - Just the appendix.
