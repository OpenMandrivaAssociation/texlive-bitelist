%global tl_name bitelist
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Split list, in TeXs mouth
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/bitelist
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bitelist.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bitelist.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bitelist.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands for "splitting" a token list at the first
occurrence of another (specified) token list. I.e., for given token
lists s, t return b and the shortest a, such that t = a s b. The
package's mechanism differs from those of packages providing similar
features, in the following ways: the method uses TeX's mechanism of
reading delimited macro parameters; splitting macros work by pure
expansion, without assignments; the operation is carried out in a single
macro call. A variant of the operation is provided, that retains outer
braces.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/bitelist
%dir %{_datadir}/texmf-dist/source/generic/bitelist
%dir %{_datadir}/texmf-dist/tex/generic/bitelist
%doc %{_datadir}/texmf-dist/doc/generic/bitelist/README
%doc %{_datadir}/texmf-dist/doc/generic/bitelist/bitelist.pdf
%doc %{_datadir}/texmf-dist/source/generic/bitelist/bitelist.tex
%doc %{_datadir}/texmf-dist/source/generic/bitelist/srcfiles.tex
%{_datadir}/texmf-dist/tex/generic/bitelist/bitedemo.tex
%{_datadir}/texmf-dist/tex/generic/bitelist/bitelist.sty
