%global tl_name c-pascal
%global tl_revision 18337

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Typeset Python, C and Pascal programs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/c_pascal
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/c-pascal.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/c-pascal.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A TeX macro package for easy typesetting programs in Python, C and
Pascal. Program source files may also be input.

