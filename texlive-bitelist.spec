Name:		texlive-bitelist
Version:	25779
Release:	1
Summary:	Split list, in TeX's mouth
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/bitelist
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bitelist.r25779.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bitelist.doc.r25779.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bitelist.source.r25779.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
