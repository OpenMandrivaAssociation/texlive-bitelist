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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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

