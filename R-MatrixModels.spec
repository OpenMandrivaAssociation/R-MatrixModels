%global packname  MatrixModels
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.3_1
Release:          3
Summary:          Modelling with Sparse And Dense Matrices
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-1.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-stats
Requires:         R-utils
Requires:         R-methods
Requires:         R-Matrix 
BuildRequires:    R-devel
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex
BuildRequires:    R-stats
BuildRequires:    R-utils
BuildRequires:    R-methods
BuildRequires:    R-Matrix
BuildRequires:    pkgconfig(lapack)

%description
Modelling with sparse and dense 'Matrix' matrices, using modular
prediction and response module classes.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3_1-1
+ Revision: 776204
- Import R-MatrixModels
- Import R-MatrixModels

