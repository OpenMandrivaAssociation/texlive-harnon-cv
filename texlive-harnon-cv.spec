# revision 26543
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-harnon-cv
Version:	20120809
Release:	9
Summary:	TeXLive harnon-cv package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harnon-cv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harnon-cv.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive harnon-cv package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/harnon-cv/harnon-cv.cls
%doc %{_texmfdistdir}/doc/latex/harnon-cv/README
%doc %{_texmfdistdir}/doc/latex/harnon-cv/sample.pdf
%doc %{_texmfdistdir}/doc/latex/harnon-cv/sample.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120809-1
+ Revision: 813559
- Import texlive-harnon-cv
- Import texlive-harnon-cv

