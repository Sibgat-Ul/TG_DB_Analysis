# Full Table Inventory (auto-generated)

Database `ocms` (MariaDB / InnoDB) - 559 tables, 22,998,166 rows total.

`last data` = MAX of the best date column in the table (recency proxy). "-" = no date column or empty.


## 01 System / Admin / Auth - 16 tables, 4,702,753 rows

| table | rows | cols | last data |
|---|--:|--:|---|
| `activity_log` | 4,654,573 | 5 | 2026 |
| `dbModulePermission` | 33,199 | 15 | 2026 |
| `dbUserRollPerm` | 12,254 | 12 | 2026 |
| `dbModuleSubSec` | 1,016 | 14 | 2026 |
| `dbProjectPermission` | 743 | 5 | 2026 |
| `dbadministrator` | 283 | 22 | 2026 |
| `dbModuleSub` | 215 | 12 | 2026 |
| `dbUserRoll` | 194 | 2 | - |
| `dbProjectCapacity` | 158 | 14 | 2025 |
| `user_other_permissions` | 42 | 7 | 2026 |
| `dbUserDepartment` | 31 | 7 | 2014 |
| `dbModule` | 15 | 9 | 2025 |
| `dbUserDesignation` | 14 | 7 | 2014 |
| `dbProjectInfo` | 13 | 18 | 2025 |
| `other_permissions` | 3 | 12 | 2023 |
| `ocmsProfile` | 0 | 10 | - |

## 02 Reference / Lookup (lib*) - 129 tables, 78,970 rows

| table | rows | cols | last data |
|---|--:|--:|---|
| `lib_color_panton` | 20,901 | 3 | - |
| `yarntest` | 17,861 | 19 | - |
| `lib_gen_size` | 5,813 | 8 | 2026 |
| `libsupplier` | 4,057 | 18 | 2026 |
| `lib_color` | 3,684 | 10 | 2026 |
| `lib_yarn_store_location` | 3,649 | 14 | 2026 |
| `lib_yarn_price` | 3,641 | 9 | 2026 |
| `libTnaBulk` | 2,924 | 15 | - |
| `lib_gen_color` | 2,189 | 8 | 2026 |
| `lib_supplier` | 2,146 | 16 | 2026 |
| `libyarncountprice` | 1,399 | 8 | 2025 |
| `libDyeingChemicalName` | 1,046 | 13 | 2026 |
| `libYDInvProductItem` | 756 | 8 | 2015 |
| `libtrimsitem` | 690 | 14 | 2020 |
| `yarn_test_report_result` | 687 | 11 | 2026 |
| `lib_rack_info` | 650 | 7 | 2018 |
| `libdia` | 472 | 6 | 2023 |
| `libDyeingChemicalLocal` | 471 | 10 | 2026 |
| `libDyeingReceipe` | 405 | 23 | 2023 |
| `libDyeingChemicalAgent` | 397 | 9 | 2026 |
| `lib_yarn_store_location_sub` | 282 | 16 | 2026 |
| `lib_size` | 245 | 6 | 2026 |
| `lib_income_expense_unit_head_dtls` | 237 | 10 | - |
| `libstructure` | 234 | 9 | 2030 |
| `libpartusage` | 216 | 5 | 2026 |
| `libyarntype` | 211 | 6 | 2026 |
| `lib_style` | 209 | 7 | 2026 |
| `libbuyerSampleStep` | 207 | 11 | 2018 |
| `libbuyer` | 194 | 19 | 2026 |
| `libKnittingMCProfile` | 175 | 21 | 2026 |
| `libgsm` | 168 | 5 | 2025 |
| `libyarncomposition` | 152 | 5 | 2026 |
| `libDyeingChemicalClass` | 137 | 8 | 2026 |
| `Lib_dying_mc_Loading` | 137 | 12 | 2014 |
| `libpartusage_api` | 125 | 5 | - |
| `lib_income_expense_unit_head` | 108 | 10 | 2025 |
| `libSignature` | 102 | 5 | - |
| `libknittargetprod` | 94 | 36 | 2017 |
| `libFloorInfo` | 86 | 13 | 2025 |
| `lib_brand` | 85 | 6 | 2026 |
| `lib_style_dept` | 83 | 6 | 2024 |
| `libMerchendisingTeam` | 82 | 10 | 2026 |
| `libUserDesignation` | 72 | 7 | 2026 |
| `libyarncount` | 71 | 7 | 2025 |
| `lib_category` | 62 | 6 | 2024 |
| `libDyeingMCLoading` | 61 | 13 | 2024 |
| `libbuyerYD` | 58 | 12 | 2014 |
| `libSampleType` | 51 | 5 | 2025 |
| `lib_packheads` | 49 | 35 | 2023 |
| `libGenUserDepartment` | 46 | 10 | 2024 |
| `libUserDepartment` | 45 | 7 | 2023 |
| `lib_emblishment` | 44 | 7 | 2021 |
| `lib_season` | 41 | 6 | 2026 |
| `libbank` | 39 | 15 | 2023 |
| `liblycraratio` | 39 | 5 | 2025 |
| `lib_commercialinvoicetexts` | 39 | 10 | 2023 |
| `libfinishing` | 34 | 7 | 2026 |
| `lib_dyeing_prod_variable` | 32 | 9 | 2024 |
| `libDyeingReceipeStep` | 31 | 8 | 2023 |
| `libDyeingMCCategory` | 30 | 8 | 2022 |
| `libDyeingReceipeClass` | 30 | 10 | 2026 |
| `libTnaStep` | 29 | 16 | 2015 |
| `libBuyingAgent` | 28 | 12 | 2025 |
| `lib_belt` | 28 | 3 | - |
| `lib_dyeing_quality_step` | 28 | 8 | 2022 |
| `lib_yarn_upcharge` | 26 | 6 | 2026 |
| `libSewingLeadTime` | 25 | 6 | - |
| `lib_yarn_type` | 24 | 4 | 2026 |
| `libLearningCurveLean` | 23 | 9 | - |
| `libTrimsUnit` | 23 | 5 | 2014 |
| `libcolordepth` | 21 | 10 | 2022 |
| `libSewingHour` | 20 | 3 | - |
| `lib_income_expense_cost_type` | 20 | 8 | 2025 |
| `libTermsCondition` | 19 | 7 | 2025 |
| `libYDInvProductGroup` | 18 | 5 | 2015 |
| `libaop` | 17 | 7 | 2025 |
| `libDyeingChemicalType` | 17 | 7 | 2026 |
| `libKnittingMCType` | 16 | 5 | 2023 |
| `libGeneralProductGroup` | 15 | 5 | 2018 |
| `libGeneralProductItem` | 15 | 8 | 2018 |
| `lib_commercialforwardtexts` | 15 | 10 | - |
| `lib_emblishment_type` | 15 | 4 | 2025 |
| `lib_pay_term` | 15 | 6 | 2025 |
| `libcolcuf` | 14 | 7 | 2021 |
| `libCountry` | 14 | 5 | 2025 |
| `libwashing` | 13 | 7 | 2023 |
| `libNoteColum` | 12 | 4 | 2014 |
| `libNoteDepartment` | 10 | 4 | 2014 |
| `libincoterm` | 9 | 5 | 2026 |
| `libRcvIssueAllowDate` | 9 | 11 | 2025 |
| `lib_income_expense_unit` | 9 | 8 | 2025 |
| `libpricetype` | 8 | 7 | 2025 |
| `lib_style_unit` | 8 | 6 | 2025 |
| `lib_yarn_country` | 8 | 4 | 2025 |
| `libpricetypemer` | 7 | 6 | 2022 |
| `lib_style_group` | 7 | 6 | 2021 |
| `libcountry_block` | 6 | 6 | 2025 |
| `libmeasurement` | 6 | 5 | 2021 |
| `libshipmode` | 6 | 5 | 2020 |
| `libydbatchstatus` | 6 | 7 | - |
| `libTrimsItemType` | 5 | 5 | 2021 |
| `lib_yarn_purchase_purpose` | 5 | 5 | 2026 |
| `libAccExpTypeDaily` | 4 | 3 | - |
| `libAccExpTypeMonthly` | 4 | 3 | - |
| `libDyeingBatchStatus` | 4 | 5 | 2014 |
| `libgarmentspart` | 4 | 5 | 2021 |
| `libLabDyesChem` | 4 | 4 | 2023 |
| `libqtytype` | 4 | 5 | 2020 |
| `libTrimsType` | 4 | 5 | 2022 |
| `lib_port_of_loading` | 4 | 6 | 2021 |
| `lib_store_location_sub` | 4 | 10 | 2026 |
| `libknitproject` | 3 | 11 | 2020 |
| `lib_pack_templates` | 3 | 11 | 2023 |
| `lib_production_variable` | 3 | 6 | 2024 |
| `libcolorprocess` | 2 | 5 | 2013 |
| `libfabrictype` | 2 | 7 | 2013 |
| `libProjectInfo` | 2 | 12 | 2014 |
| `libSampleDyeMatch` | 2 | 5 | 2015 |
| `libTrimsSupp` | 2 | 10 | - |
| `libydstripe` | 2 | 5 | 2013 |
| `lib_commcert` | 2 | 18 | - |
| `lib_commforward` | 2 | 17 | 2022 |
| `lib_pack_head_foot` | 2 | 15 | 2022 |
| `lib_pack_head_foot_vals` | 2 | 11 | 2022 |
| `lib_suppliersCategory` | 2 | 5 | - |
| `libDyeingHourCost` | 1 | 3 | 2022 |
| `libmarketingteam` | 1 | 14 | - |
| `lib_commercialcerttext` | 1 | 10 | 2022 |
| `lib_comm_pay_term` | 0 | 6 | - |

## 03 Core OCMS - Orders/TNA/Approvals/Products - 31 tables, 3,994,828 rows

| table | rows | cols | last data |
|---|--:|--:|---|
| `ocms_doc_approval_sts` | 1,691,791 | 9 | - |
| `ocms_chemical_transaction` | 1,333,513 | 8 | 3023 |
| `ocms_purchase_requisition_approval` | 767,544 | 12 | 2026 |
| `ocms_orderTnaTable` | 156,816 | 39 | - |
| `income_expense_month_details` | 20,184 | 16 | 2026 |
| `turag_stock_value_summary_dtls` | 14,384 | 8 | 2026 |
| `ocms_product_info` | 7,245 | 22 | 2026 |
| `ocms_doc_approval` | 826 | 12 | 2026 |
| `ocms_prod_specification` | 691 | 8 | 2026 |
| `ocms_tna_leadtime_library` | 506 | 19 | - |
| `ocms_home_summary` | 432 | 12 | - |
| `ocms_prod_used_for` | 278 | 8 | 2026 |
| `general_used_for2` | 215 | 10 | 2023 |
| `ocms_prod_category` | 184 | 9 | 2025 |
| `ocms_measurement_unit` | 47 | 7 | 2022 |
| `ocms_tna_comments` | 39 | 8 | 2024 |
| `ocms_product_group` | 34 | 8 | 2023 |
| `turag_stock_value_summary` | 32 | 12 | 2025 |
| `ocms_tna_step` | 22 | 8 | 2020 |
| `ocms_prod_agent` | 21 | 8 | 2025 |
| `general_currency_conversion` | 17 | 10 | 2025 |
| `mer_currency_conversion` | 3 | 10 | 2025 |
| `ocms_doc_condition` | 3 | 8 | 2022 |
| `general_used_for` | 1 | 9 | 2023 |
| `ocms_product_details` | 0 | 9 | - |
| `ocms_product_supplier` | 0 | 7 | - |
| `ocms_purchase_requisition` | 0 | 18 | - |
| `ocms_purchase_requisition_details` | 0 | 20 | - |
| `ocms_requisition_quote` | 0 | 13 | - |
| `ocms_requisition_quote_approval` | 0 | 6 | - |
| `ocms_supplier_profile` | 0 | 16 | - |

## 04 Sampling / Development / Inquiry - 59 tables, 369,528 rows

| table | rows | cols | last data |
|---|--:|--:|---|
| `sample_yarnselection` | 88,896 | 30 | 2026 |
| `sample_breakdown_info` | 46,482 | 35 | - |
| `sample_trims_info` | 44,543 | 22 | - |
| `sample_fabricationinfodetails` | 42,284 | 51 | 2026 |
| `requisitioncuttingdetails` | 37,846 | 23 | 2026 |
| `sample_fabricationinfo` | 28,308 | 36 | 2026 |
| `sample_type_info` | 18,762 | 7 | 2026 |
| `sample_basic_info` | 14,010 | 49 | - |
| `sub_fabricationinfodetails` | 10,800 | 33 | 2026 |
| `short_yarnselection` | 5,989 | 30 | 2026 |
| `short_breakdown_info` | 5,768 | 23 | - |
| `sample_ydcombo` | 5,269 | 34 | 2026 |
| `short_fabricationinfodetails` | 3,323 | 52 | 2026 |
| `sub_basic_info` | 3,201 | 22 | 2026 |
| `sample_collarcuffinfo` | 2,355 | 19 | 2026 |
| `requisitioncutting` | 2,260 | 14 | 2026 |
| `short_basic_info` | 2,120 | 30 | 2026 |
| `dev_yarnselection` | 1,545 | 31 | 2025 |
| `dev_breakdown_info` | 949 | 35 | - |
| `dev_fabricationinfodetails` | 887 | 60 | 2025 |
| `short_collarcuffinfo` | 818 | 21 | 2026 |
| `dev_fabricationinfo` | 697 | 36 | 2025 |
| `sample_emblishment_info` | 517 | 15 | 2023 |
| `dev_basic_info` | 471 | 51 | - |
| `short_ydcombo` | 364 | 31 | 2026 |
| `sample_trims_info_details` | 194 | 16 | - |
| `strims_trims_info_details` | 180 | 18 | - |
| `strims_basic_info` | 144 | 18 | 2023 |
| `dev_ydcombo` | 122 | 30 | 2023 |
| `inq_po_sheet` | 119 | 5 | - |
| `sample_budgetCostsheet` | 97 | 34 | 2025 |
| `strims_trims_info` | 73 | 20 | - |
| `inq_breakdown_info` | 46 | 35 | - |
| `dev_trims_info` | 30 | 21 | - |
| `dev_collarcuffinfo` | 26 | 18 | 2023 |
| `inq_trims_info` | 5 | 21 | - |
| `requisitiondyeingfabric` | 5 | 13 | 2022 |
| `inq_fabricationinfo` | 4 | 36 | 2025 |
| `mkt_basic_info` | 4 | 46 | - |
| `mkt_cost_info` | 4 | 33 | 2025 |
| `dev_emblishment_info` | 3 | 15 | 2020 |
| `inq_emblishment_info` | 3 | 15 | 2020 |
| `inq_basic_info` | 1 | 50 | - |
| `inq_fabricationinfodetails` | 1 | 60 | 2025 |
| `inq_yarnselection` | 1 | 29 | 2025 |
| `mkt_fabric_info` | 1 | 15 | 2025 |
| `requisitiondyeingfabricdetails` | 1 | 13 | - |
| `dev_po_sheet` | 0 | 5 | - |
| `dev_trims_info_details` | 0 | 16 | - |
| `inq_collarcuffinfo` | 0 | 18 | - |
| `inq_trims_info_details` | 0 | 16 | - |
| `inq_ydcombo` | 0 | 30 | - |
| `mkt_style_info` | 0 | 27 | - |
| `mkt_trims_info` | 0 | 15 | - |
| `sample_po_sheet` | 0 | 5 | - |
| `short_emblishment_info` | 0 | 15 | - |
| `subcontract_basic_info` | 0 | 22 | - |
| `subcontract_fabric_info` | 0 | 36 | - |
| `sub_breakdown_info` | 0 | 38 | - |

## 05 Bulk Order / Costing - 22 tables, 1,288,058 rows

| table | rows | cols | last data |
|---|--:|--:|---|
| `bulk_trims_info_details` | 725,605 | 18 | - |
| `bulk_trims_info` | 124,630 | 25 | - |
| `bulk_breakdown_info` | 122,834 | 52 | - |
| `bulk_emblishment_info` | 95,296 | 24 | 2026 |
| `bulk_yarnselection` | 79,683 | 38 | 2026 |
| `bulk_fabricationinfodetails` | 50,933 | 76 | 2026 |
| `bulk_fabricationinfo` | 24,364 | 40 | 2026 |
| `bulk_collarcuffinfo` | 12,575 | 21 | 2026 |
| `bulk_po_sheet` | 8,848 | 5 | - |
| `order_lineLoading` | 8,554 | 21 | 2024 |
| `bulk_basic_info` | 7,187 | 78 | - |
| `bulk_budgetCostActual` | 7,165 | 26 | - |
| `bulk_budgetCostsheet` | 7,164 | 49 | 2026 |
| `bulk_ydcombo` | 3,679 | 38 | 2026 |
| `bulk_budgetCostShortActual` | 3,483 | 25 | - |
| `bulk_others_cost` | 2,316 | 11 | 2026 |
| `bulk_sample_type_info` | 1,565 | 9 | 2026 |
| `order_linePlan` | 1,177 | 20 | 2024 |
| `bulk_sample_breakdown_info` | 731 | 15 | - |
| `order_tnaInfo` | 248 | 18 | 2025 |
| `bulk_cost_sheet` | 13 | 5 | - |
| `bulk_dhl_info` | 8 | 18 | 2026 |

## 06 Work Order - 41 tables, 731,704 rows

| table | rows | cols | last data |
|---|--:|--:|---|
| `workorder_trimsDetails` | 171,804 | 34 | 2026 |
| `workorder_knittingDetails` | 112,180 | 55 | 2026 |
| `work_order_document` | 86,399 | 5 | - |
| `workorder_sampleDetails` | 76,319 | 19 | 2026 |
| `workorder_emblishmentDetails` | 42,407 | 24 | 2026 |
| `workorder_cmtTrims` | 37,014 | 21 | 2026 |
| `workorder_knitting` | 34,013 | 27 | 2026 |
| `workorder_trims` | 33,809 | 44 | 2026 |
| `workorder_knittingCollarYd` | 24,660 | 18 | 2026 |
| `workorder_embdDetails` | 22,355 | 24 | 2026 |
| `workorder_cmtDetails` | 20,150 | 17 | 2026 |
| `workorder_knittingCollarInfo` | 20,013 | 21 | 2026 |
| `workorder_sample` | 14,287 | 24 | 2026 |
| `workorder_yarnDyeingDetails` | 8,437 | 37 | 2026 |
| `workorder_cmtFabric` | 7,168 | 22 | 2026 |
| `workorder_fabricDetails` | 6,230 | 25 | 2026 |
| `workorder_emblishment` | 2,573 | 30 | 2026 |
| `workorder_yarnDyeing` | 2,443 | 45 | 2026 |
| `workorder_cmt` | 2,322 | 22 | 2026 |
| `workorder_aopDetails` | 1,816 | 23 | 2026 |
| `workorder_embd` | 1,762 | 43 | 2026 |
| `workorder_fabric` | 1,415 | 33 | 2026 |
| `workorder_aop` | 1,163 | 43 | 2026 |
| `workorder_tippingDetails` | 509 | 19 | 2025 |
| `workorder_embdFabric` | 115 | 22 | - |
| `workorder_tipping` | 93 | 22 | 2025 |
| `wo_TrimsPront` | 55 | 20 | - |
| `wo_FabricPrint` | 40 | 20 | 2024 |
| `workorder_printDetails` | 37 | 24 | 2020 |
| `workorder_finishing` | 32 | 42 | 2022 |
| `wo_FabricPrintDetails` | 29 | 32 | 2024 |
| `workorder_print` | 24 | 42 | 2020 |
| `workorder_washing` | 15 | 42 | 2021 |
| `workorder_washingDetails` | 9 | 25 | 2021 |
| `workorder_twisting` | 3 | 17 | 2021 |
| `workorder_twistingDetails` | 3 | 21 | 2021 |
| `wo_TrimsProntDetails` | 1 | 26 | - |
| `workorder_emblishmentFabric` | 0 | 23 | - |
| `workorder_finishingDetails` | 0 | 24 | - |
| `workorder_yarn` | 0 | 12 | - |
| `workorder_yarnDetails` | 0 | 14 | - |

## 07 Knitting - 35 tables, 934,025 rows

| table | rows | cols | last data |
|---|--:|--:|---|
| `knitting_prod_mc_dtls` | 260,994 | 17 | 2026 |
| `knitting_fabricRcvDetails` | 145,396 | 30 | 2026 |
| `knitting_delivaryChalanDetails` | 145,364 | 30 | 2026 |
| `knittingYarnAllocation` | 128,755 | 51 | 2026 |
| `knitting_target_dtl` | 90,037 | 19 | - |
| `knitting_prod_mcwise` | 86,705 | 34 | - |
| `knitting_target` | 38,150 | 23 | - |
| `knitting_fabricRcv` | 16,634 | 19 | 2026 |
| `knitting_delivaryChalan` | 7,284 | 21 | 2026 |
| `knitting_target_yds_dtl` | 3,647 | 20 | - |
| `knitting_target_yds` | 3,485 | 24 | - |
| `knitting_prod_mcwise_yds` | 3,470 | 38 | - |
| `knitting_prod_mc_dtls_yds` | 3,446 | 18 | 2026 |
| `knitting_dailyProductionCollar` | 381 | 24 | - |
| `knitting_target_collar` | 148 | 26 | - |
| `knitting_subContract` | 50 | 39 | 2021 |
| `knitting_target_collar_dtl` | 40 | 22 | - |
| `knitting_prod_mcwise_collar` | 36 | 41 | - |
| `knit_currency_conversion` | 2 | 10 | 2024 |
| `knitting_prod_mc_dtls_pcs` | 1 | 18 | 2024 |
| `knitting_dailyProduction` | 0 | 25 | - |
| `knitting_dailyTarget` | 0 | 21 | - |
| `knitting_dailyTargetF` | 0 | 28 | - |
| `knitting_delivaryChalanCollar` | 0 | 16 | - |
| `knitting_fabricRcvCollar` | 0 | 18 | - |
| `knitting_monthlyLoad` | 0 | 15 | - |
| `knitting_productionPlan` | 0 | 20 | - |
| `knitting_program_production` | 0 | 22 | - |
| `knitting_program_prod_collar` | 0 | 20 | - |
| `knitting_subContractCollar` | 0 | 16 | - |
| `knitting_target_daily` | 0 | 25 | - |
| `knit_qad` | 0 | 24 | - |
| `knit_qad_rolls` | 0 | 28 | - |
| `knit_target` | 0 | 40 | - |
| `knit_target_yarns` | 0 | 10 | - |

## 08 Dyeing & Finishing - 53 tables, 2,563,321 rows

| table | rows | cols | last data |
|---|--:|--:|---|
| `dyeing_batchReceipe` | 1,309,633 | 55 | 2026 |
| `dyeing_processStatus` | 271,725 | 44 | 2026 |
| `dyeing_batchQuality` | 198,778 | 40 | - |
| `dyeing_batchCard` | 131,470 | 37 | 2026 |
| `dyeing_batchCardCollar` | 82,267 | 13 | 2026 |
| `dyeing_finishProd` | 78,864 | 42 | - |
| `dyeing_batchPlan` | 74,362 | 72 | 2026 |
| `dyeing_process_requisition_dtls` | 71,572 | 27 | 2026 |
| `dyeing_prodStatus` | 68,167 | 11 | - |
| `dyeing_fabricDelivaryDetails` | 36,523 | 34 | 2026 |
| `finish_fabricRcvDetails` | 34,166 | 36 | 2026 |
| `dyeing_turag_process_requisition_dtls` | 29,528 | 23 | 2026 |
| `finishing_process_requisition_dtls` | 24,049 | 29 | 2026 |
| `dyeing_batchFabricChalanDetails` | 18,272 | 30 | 2026 |
| `dyeing_process_requisition` | 17,962 | 20 | 2026 |
| `finishing_process_requisition` | 12,758 | 21 | 2026 |
| `dyeing_fabricRcvDetails` | 11,553 | 31 | 2026 |
| `dyeing_turag_fabricRcvDetails` | 11,221 | 31 | 2026 |
| `dyeing_turagFabricChalanDetails` | 11,186 | 33 | 2026 |
| `finish_fabricRcv` | 10,850 | 24 | 2026 |
| `dyeing_fabricDelivary` | 10,263 | 24 | 2026 |
| `dyeing_batchFabricChalan` | 9,104 | 24 | 2026 |
| `dyeing_turag_fabricRcvGreyDetails` | 5,716 | 25 | 2026 |
| `dyeing_finishingRecipe` | 5,521 | 14 | 2022 |
| `dyeing_fabricRcv` | 4,794 | 24 | 2026 |
| `dyeing_turag_process_requisition` | 4,542 | 20 | 2026 |
| `dyeing_turagFabricGreyChalanDetails` | 2,468 | 29 | 2026 |
| `dyeing_turagFabricChalan` | 2,375 | 26 | 2026 |
| `dyeing_turag_fabricRcvGrey` | 2,355 | 22 | 2026 |
| `dyeing_turag_fabricRcv` | 2,320 | 24 | 2026 |
| `chemical_spr_body` | 2,180 | 14 | 2026 |
| `chemical_wo_body` | 2,043 | 18 | 2026 |
| `dyeing_turagFabricGreyChalan` | 1,118 | 26 | 2026 |
| `chemical_wo_head` | 1,052 | 26 | 2026 |
| `dyeing_process_requ_collar` | 868 | 19 | 2021 |
| `dyeing_batchInspection` | 825 | 33 | 2025 |
| `chemical_spr_head` | 447 | 17 | 2026 |
| `dyeing_fabricRcvCollar` | 147 | 19 | 2021 |
| `dyeing_labBatch` | 110 | 18 | 2021 |
| `dyeing_batchFabricChalanCollar` | 51 | 19 | 2021 |
| `finishing_process_requ_collar` | 43 | 19 | 2024 |
| `dyeing_fabricatioInfo` | 36 | 26 | - |
| `dyeing_labFileTrakingDetails` | 12 | 11 | - |
| `dyeing_labSampleTraking` | 10 | 19 | - |
| `dyeing_orderInfo` | 7 | 24 | - |
| `dyeing_labtesting` | 6 | 18 | 2020 |
| `dyeing_labFileTraking` | 2 | 24 | - |
| `dyeing_fabricDelivaryCollar` | 0 | 20 | - |
| `dyeing_finishDelivaryChalan` | 0 | 18 | - |
| `dyeing_finishingProduction` | 0 | 9 | - |
| `dyeing_finishRoll` | 0 | 17 | - |
| `dyeing_labReceipe` | 0 | 20 | - |
| `finish_fabricRcvCollar` | 0 | 21 | - |

## 09 Production (Cut/Sew/Finish) - 14 tables, 3,068,122 rows

| table | rows | cols | last data |
|---|--:|--:|---|
| `production_sewingInfoDetails` | 2,175,886 | 19 | 2026 |
| `production_cuttingInfo` | 369,173 | 19 | 2026 |
| `production_sewingInput` | 138,309 | 19 | 2025 |
| `production_finishingInfo` | 129,171 | 20 | 2026 |
| `production_cuttingTarget` | 118,530 | 26 | 2026 |
| `production_sewingInfo` | 70,076 | 51 | 2026 |
| `production_fabricReceiveDetails` | 53,429 | 33 | 2026 |
| `production_finishingCtn` | 10,305 | 14 | 2026 |
| `production_cuttingTargetOther` | 1,660 | 17 | 2026 |
| `production_fabricReceive` | 1,305 | 13 | 2026 |
| `prod_brush_belt` | 140 | 7 | 2024 |
| `production_finishingTarget` | 95 | 12 | 2024 |
| `production_fabricIssueDetails` | 36 | 36 | 2025 |
| `production_fabricIssue` | 7 | 22 | 2025 |

## 10 Inventory & Store - 123 tables, 5,265,690 rows

| table | rows | cols | last data |
|---|--:|--:|---|
| `inventory_DyesChemIssueDetailsSub` | 1,301,938 | 26 | 2026 |
| `inventory_trimsIssueDetails` | 449,392 | 37 | 2026 |
| `inventory_GeneralIssueDetails` | 367,393 | 46 | 2026 |
| `invoice_mrr_info_dtls` | 301,344 | 38 | 2026 |
| `inventory_trimsReceiveDetails` | 187,626 | 31 | 2026 |
| `inventory_trimsIssue` | 154,720 | 25 | 2026 |
| `inventory_printIssueDetails` | 151,665 | 27 | 2026 |
| `inventory_grayFabricReceiveDetails` | 149,425 | 49 | 2026 |
| `inventory_GeneralIssue` | 132,618 | 31 | 2026 |
| `inventory_shipmentIssueDetails` | 127,325 | 24 | 2026 |
| `inventory_yarnIssueDetails` | 121,683 | 43 | 2026 |
| `inventory_finishFabricIssueDetails` | 112,957 | 40 | 2026 |
| `inventory_grayFabricIssueDetails` | 111,610 | 39 | 2026 |
| `inventory_finishFabricReceiveDetails` | 110,314 | 43 | 2026 |
| `inventory_DyesChemIssueSub` | 110,302 | 19 | 2026 |
| `inv_gatePassDetails` | 98,734 | 20 | 2026 |
| `inventory_GeneralReceiveDetails` | 81,511 | 55 | 2026 |
| `inv_purchase_requisition` | 74,122 | 52 | 2026 |
| `inventory_trimsReceive` | 68,771 | 24 | 2026 |
| `inventory_embdReceiveDetails` | 62,490 | 22 | 2026 |
| `inv_general_wo_dtl` | 59,986 | 30 | 2026 |
| `inventory_embdIssueDetails` | 59,633 | 27 | 2026 |
| `inventory_yarnIssue` | 56,235 | 25 | 2026 |
| `inventory_DyesChemIssueDetails` | 54,124 | 20 | 2026 |
| `inventory_shipmentRcvDetails` | 52,965 | 23 | 2026 |
| `inventory_GeneralReceiveDetails_c` | 50,446 | 51 | 2024 |
| `inventory_grayFabricIssue` | 46,544 | 24 | 2026 |
| `inventory_grayFabricReceive` | 43,359 | 20 | 2026 |
| `inventory_yarnReceiveDetails` | 37,710 | 40 | 2026 |
| `inventory_yarnReceive` | 34,845 | 28 | 2026 |
| `inv_gatePass` | 33,036 | 13 | 2026 |
| `inventory_DyesChemSubRcvDetails` | 32,759 | 17 | 2026 |
| `inventory_DyesChemSubRequ` | 31,086 | 20 | 2026 |
| `inventory_printIssue` | 30,454 | 24 | 2026 |
| `inventory_GeneralReceive` | 27,701 | 34 | 2026 |
| `inventory_printReceiveDetails` | 27,217 | 29 | 2026 |
| `inv_general_wo` | 20,732 | 44 | 2026 |
| `invoice_mrr_info` | 17,893 | 22 | 2026 |
| `inventory_cmtReceiveDetails` | 17,322 | 25 | 2026 |
| `inv_service_requisition` | 16,948 | 45 | - |
| `inventory_GeneralReceive_c` | 16,819 | 34 | 2024 |
| `inventory_finishFabricReceive` | 15,691 | 24 | 2026 |
| `inventory_grayFabricCollarRcv` | 13,730 | 20 | 2026 |
| `inventory_ydReceiveDetails` | 13,668 | 37 | 2026 |
| `inventory_finishFabricIssue` | 13,086 | 23 | 2026 |
| `inventory_shipmentIssue` | 12,184 | 33 | 2026 |
| `stock_yarn_store` | 11,531 | 24 | - |
| `inventory_DyesChemIssue` | 11,065 | 20 | 2026 |
| `inventory_ydIssueDetails` | 10,469 | 34 | 2026 |
| `inventory_cmtIssueDetails` | 10,421 | 29 | 2026 |
| `invoice_mrr_info_collar` | 9,284 | 20 | 2026 |
| `inventory_embdReceive` | 9,236 | 25 | 2026 |
| `inventory_embdIssue` | 8,662 | 24 | 2026 |
| `inventory_ydReceive` | 6,996 | 15 | 2026 |
| `inventory_DyesChemReceiveDetails` | 6,024 | 22 | 2026 |
| `inventory_grayFabricCollarIssue` | 5,760 | 16 | 2024 |
| `inventory_finishFabricCollarRcv` | 5,044 | 17 | 2026 |
| `inventory_finishFabricCollarIssue` | 4,937 | 17 | 2026 |
| `inventory_shipmentRcv` | 4,462 | 15 | 2026 |
| `inv_yarn_test_dtls` | 4,286 | 43 | 2026 |
| `inventory_printReceive` | 4,148 | 25 | 2026 |
| `inventory_ydIssue` | 3,858 | 20 | 2026 |
| `inventory_smokingIssueDetails` | 3,638 | 21 | 2026 |
| `inv_purchase_wo_dtl` | 3,450 | 29 | 2026 |
| `inventory_DyesChemReceive` | 3,254 | 23 | 2026 |
| `inventory_cmtReceive` | 3,123 | 24 | 2026 |
| `inv_yarn_test` | 3,038 | 21 | 2026 |
| `inventory_grIssueDetails` | 2,617 | 20 | 2026 |
| `stock_dyesChemSub` | 2,134 | 10 | - |
| `inventory_DyesChemSubRcv` | 1,941 | 23 | 2026 |
| `inv_yarn_purchase_requisition` | 1,801 | 69 | - |
| `inventory_serviceReceiveDetails` | 1,750 | 27 | 2026 |
| `inv_purchase_wo` | 1,476 | 37 | 2026 |
| `inventory_serviceReceive` | 1,402 | 18 | 2026 |
| `inventory_grReceiveDetails` | 1,210 | 22 | 2026 |
| `inventory_smokingReceiveDetails` | 1,156 | 23 | 2026 |
| `inventory_cmtIssue` | 988 | 24 | 2026 |
| `inventory_smokingIssue` | 671 | 24 | 2026 |
| `inventory_tippingReceiveDetails` | 657 | 21 | 2025 |
| `inventory_tippingIssueDetails` | 598 | 20 | 2025 |
| `inventory_tippingFloorDetails` | 491 | 18 | 2025 |
| `inventory_grReceive` | 376 | 24 | 2026 |
| `inventory_grIssue` | 374 | 23 | 2026 |
| `inventory_smokingReceive` | 225 | 25 | 2026 |
| `inventory_tippingReceive` | 150 | 24 | 2025 |
| `inv_gatePassTrims` | 134 | 14 | 2025 |
| `inv_gatePassTrimsDetails` | 133 | 24 | 2025 |
| `inventory_tippingFloor` | 131 | 23 | 2025 |
| `inventory_generalRequisitionDetails` | 107 | 28 | 2025 |
| `inventory_finish_goods_rcv_dtls` | 96 | 20 | 2025 |
| `inventory_finishGoodsIssueDetails` | 91 | 21 | 2025 |
| `inventory_tippingIssue` | 78 | 22 | 2025 |
| `inventory_generalRequisition` | 67 | 25 | 2025 |
| `invoice_wo_info_dtls` | 7 | 28 | 2021 |
| `inventory_knittingRequisition` | 5 | 32 | - |
| `inventory_dyeingRequisition` | 4 | 32 | - |
| `inventory_dyeingRequisitionDetails` | 4 | 30 | - |
| `inventory_finish_goods_rcv` | 3 | 13 | 2025 |
| `inventory_aopReceive` | 2 | 14 | 2020 |
| `inventory_finishGoodsIssue` | 2 | 33 | 2025 |
| `inventory_aopIssue` | 1 | 19 | 2020 |
| `inventory_aopIssueDetails` | 1 | 27 | 2020 |
| `inventory_aopReceiveDetails` | 1 | 26 | 2020 |
| `inventory_knittingRequisitionDetails` | 1 | 28 | - |
| `inventory_twistingIssue` | 1 | 25 | - |
| `inventory_twistingYarnReceive` | 1 | 28 | 2025 |
| `inventory_twistingYarnReceiveDetails` | 1 | 34 | 2025 |
| `inventory_yarnRequisition` | 1 | 41 | - |
| `invoice_wo_info` | 1 | 21 | 2021 |
| `inv_greyProcessMrr` | 1 | 16 | - |
| `inventory_embdIssueFabric` | 0 | 21 | - |
| `inventory_finishFabricOrderTransfer` | 0 | 23 | - |
| `inventory_sampleChalan` | 0 | 16 | - |
| `inventory_sampleChalanDetails` | 0 | 14 | - |
| `inventory_twistingIssueDetails` | 0 | 39 | - |
| `inventory_yarnRequisitionDetails` | 0 | 27 | - |
| `inventory_yarnTest` | 0 | 16 | - |
| `inv_greyProcessChalan` | 0 | 20 | - |
| `inv_greyProcessChalanCollar` | 0 | 17 | - |
| `inv_greyProcessChalanDetails` | 0 | 26 | - |
| `inv_greyProcessMrrCollar` | 0 | 17 | - |
| `inv_greyProcessMrrDetails` | 0 | 24 | - |
| `stock_dyesChemMain` | 0 | 7 | - |

## 11 Commercial / Invoicing / LC - 31 tables, 943 rows

| table | rows | cols | last data |
|---|--:|--:|---|
| `comm_pi_items` | 204 | 19 | 2023 |
| `comm_masterLCDetails` | 171 | 15 | - |
| `comm_piInfoDetails` | 105 | 12 | - |
| `comm_bbLC` | 85 | 53 | 2026 |
| `comm_pi` | 83 | 34 | 2023 |
| `comm_tt` | 77 | 32 | 2023 |
| `comm_file` | 51 | 9 | - |
| `comm_masterLC` | 30 | 62 | 2023 |
| `comm_ci` | 22 | 54 | 2024 |
| `comm_piInfo` | 22 | 22 | 2020 |
| `comm_masterLC_clauses` | 19 | 2 | - |
| `comm_cf` | 14 | 23 | 2023 |
| `comm_templates` | 11 | 12 | 2023 |
| `comm_masterLcInvoice` | 10 | 33 | 2022 |
| `comm_masterLCAmendment` | 9 | 18 | 2022 |
| `comm_cert` | 6 | 24 | 2022 |
| `comm_cert_templates` | 5 | 13 | 2023 |
| `comm_bblc_docs` | 3 | 14 | 2023 |
| `comm_cf_templates` | 3 | 12 | 2022 |
| `comm_masterLCDoc` | 3 | 22 | - |
| `comm_masterLcInvoiceDetails` | 3 | 14 | - |
| `comm_ci_bill_inv` | 2 | 13 | - |
| `comm_foc` | 2 | 54 | 2023 |
| `comm_masterLC_udtacks` | 2 | 2 | - |
| `comm_ci_bill` | 1 | 11 | 2023 |
| `comm_bbLCDetails` | 0 | 5 | - |
| `comm_ci_history` | 0 | 5 | - |
| `comm_foc_docs` | 0 | 14 | - |
| `comm_masterLC_discounts` | 0 | 3 | - |
| `comm_masterLC_notifyParty` | 0 | 3 | - |
| `comm_pi_block_items` | 0 | 15 | - |

## 12 Packing & Shipment - 5 tables, 224 rows

| table | rows | cols | last data |
|---|--:|--:|---|
| `packlist_datas` | 183 | 14 | - |
| `packlist_heads` | 32 | 9 | - |
| `packing_lists` | 5 | 19 | 2023 |
| `packlist_comm_vals` | 4 | 3 | - |
| `pack_attach` | 0 | 3 | - |
