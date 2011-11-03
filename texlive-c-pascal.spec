# revision 18337
# category Package
# catalog-ctan /macros/generic/c_pascal
# catalog-date 2008-01-08 01:09:19 +0100
# catalog-license pd
# catalog-version 1.2
Name:		texlive-c-pascal
Version:	1.2
Release:	1
Summary:	Typeset Python, C and Pascal programs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/c_pascal
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/c-pascal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/c-pascal.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A TeX macro package for easy typesetting programs in Python, C
and Pascal. Program source files may also be input.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/c-pascal/cap.tex
%{_texmfdistdir}/tex/generic/c-pascal/cap_c.tex
%{_texmfdistdir}/tex/generic/c-pascal/cap_comm.tex
%{_texmfdistdir}/tex/generic/c-pascal/cap_pas.tex
%{_texmfdistdir}/tex/generic/c-pascal/cap_pyt.tex
%doc %{_texmfdistdir}/doc/generic/c-pascal/README.eng
%doc %{_texmfdistdir}/doc/generic/c-pascal/README.pol
%doc %{_texmfdistdir}/doc/generic/c-pascal/demo1.tex
%doc %{_texmfdistdir}/doc/generic/c-pascal/demo2.tex
%doc %{_texmfdistdir}/doc/generic/c-pascal/prog/fib.py
%doc %{_texmfdistdir}/doc/generic/c-pascal/prog/guess.pas
%doc %{_texmfdistdir}/doc/generic/c-pascal/prog/sun.c
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
