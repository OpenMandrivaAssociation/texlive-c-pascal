# revision 18337
# category Package
# catalog-ctan /macros/generic/c_pascal
# catalog-date 2008-01-08 01:09:19 +0100
# catalog-license pd
# catalog-version 1.2
Name:		texlive-c-pascal
Version:	1.2
Release:	2
Summary:	Typeset Python, C and Pascal programs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/c_pascal
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/c-pascal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/c-pascal.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%define		_unpackaged_subdirs_terminate_build	0

%description
A TeX macro package for easy typesetting programs in Python, C
and Pascal. Program source files may also be input.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 750767
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 718162
- texlive-c-pascal
- texlive-c-pascal
- texlive-c-pascal
- texlive-c-pascal
- texlive-c-pascal

