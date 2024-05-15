# Digital Marketplace Frontend Jinja

Records breaking changes from major version bumps.

## 2.4.0rc5

Remove support for Python 3.9

Update flask support to v2.3


## 2.3.0

Add support for Python 3.12


## 2.2.0

Upgrade Digital Marketplace GOV.UK Frontend to v6.2


## 2.1.0

Use CCS GOV.UK Frontend Jinja to v1.0 (GOV.UK Frontend 5.3.1)


## 2.0.0

Upgrade GOV.UK Frontend Jinja to v3.0 (GOV.UK Frontend 5.1)


## 1.4.0

🆕 New features:

  Add macros for the following components:

  | Component name                          | Macro name                                                |
  |-----------------------------------------|-----------------------------------------------------------|
  | Compliance communication attachment row | `digitalmarketplaceComplianceCommunicationAttachmentRow`  |
  | Compliance communication attachments    | `digitalmarketplaceComplianceCommunicationAttachments`    |


## 1.2.0

Allow for use with all currently maintained Python versions:
- 3.9
- 3.10
- 3.11

Note, because ccs-digitalmarketplace-utils does not support 3.12 yet, neither can we.

## 1.1.0

Upgrade Flask to v2 and, therefore, Jinja to v3

Upgrade GOV.UK Frontend Jinja to v2.8 (GOV.UK Frontend 4.8)

## 1.0.0

🆕 New features:

  Add macros for the following components:

  | Component name            | Macro name                                  |
  |---------------------------|---------------------------------------------|
  | Alert                     | `digitalmarketplaceAlert`                   |
  | Attachment                | `digitalmarketplaceAttachment`              |
  | Banner                    | `digitalmarketplaceBanner`                  |
  | Character Count From Form | `digitalmarketplaceCharacterCountFromForm`  |
  | Checkboxes From Form      | `digitalmarketplaceCheckboxesFromForm`      |
  | Cookie Banner             | `digitalmarketplaceCookieBanner`            |
  | Documents                 | `digitalmarketplaceDocuments`               |
  | Footer                    | `digitalmarketplaceFooter`                  |
  | Header                    | `digitalmarketplaceHeader`                  |
  | Input From Form           | `digitalmarketplaceInputFromForm`           |
  | List Input                | `digitalmarketplaceListInput`               |
  | New Framework Banner      | `digitalmarketplaceNewFrameworkBanner`      |
  | Option Select             | `digitalmarketplaceOptionSelect`            |
  | Previous Next Pagination  | `digitalmarketplacePreviousNextPagination`  |
  | Question                  | `digitalmarketplaceQuestion`                |
  | Radios From Form          | `digitalmarketplaceRadiosFromForm`          |
  | Search Box                | `digitalmarketplaceSearchBox`               |
  | Select Country From Form  | `digitalmarketplaceSelectCountryFromForm`   |
  | Summary Content           | `digitalmarketplaceSummaryContent`          |
  | Temporary Message         | `digitalmarketplaceTemporaryMessage`        |

  Add the following layouts:

  - `layouts/_custom_dimensions.html`
  - `layouts/_site_verification.html`

  Add the following error page templates:

  - `errors/400.html`
  - `errors/403.html`
  - `errors/404.html`
  - `errors/410.html`
  - `errors/500.html`
