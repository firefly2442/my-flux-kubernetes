# Defect Dojo and Trivy

Defect Dojo and Trivy work together.  Trivy is a popular security scanner
that can run against container images to check for CVEs and other vulnerabilities.
Defect Dojo is a web-ui that can leverage Trivy to show lists and details of vulnerabilities
and provides a nice front-end.

Trivy security scans are done automatically through the Trivy Operator.  These
are picked up by the Trivy DefectDojo Report Operator which passes them
to the DefectDojo web-ui.  This requires a secret API key setup
in DefectDojo and setup within the Trivy DefectDojo Report Operator.

This was setup, however, the volume of scanning as well as the compute required for it all
seemed to be overkill.  Since this is all a private and local cluster, it's all
commented out for now.

## Links

* [https://defectdojo.com/](https://defectdojo.com/)
* [https://trivy.dev/](https://trivy.dev/)
