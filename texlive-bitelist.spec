# revision 25779
# category Package
# catalog-ctan /macros/generic/bitelist
# catalog-date 2012-03-29 18:26:00 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-bitelist
Version:	0.1
Release:	4
Summary:	Split list, in TeX's mouth
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/bitelist
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bitelist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bitelist.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bitelist.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands for "splitting" a token list at
the first occurrence of another (specified) token list. I.e.,
for given token lists s, t return b and the shortest a, such
that t = a s b. The package's mechanism differs from those of
packages providing similar features, in the following ways: -
the method uses TeX's mechanism of reading delimited macro
parameters; - the splitting macros work by pure expansion,
without assignments; - the operation is carried out in a single
macro call. A variant of the operation is provided, that
retains outer braces.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/bitelist/bitedemo.tex
%{_texmfdistdir}/tex/generic/bitelist/bitelist.sty
%doc %{_texmfdistdir}/doc/generic/bitelist/README
%doc %{_texmfdistdir}/doc/generic/bitelist/bitelist.pdf
#- source
%doc %{_texmfdistdir}/source/generic/bitelist/bitelist.tex
%doc %{_texmfdistdir}/source/generic/bitelist/srcfiles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 790536
- Import texlive-bitelist
- Import texlive-bitelist

