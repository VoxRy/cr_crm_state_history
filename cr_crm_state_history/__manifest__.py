# -*- coding: utf-8 -*-
# Part of Creyox Technologies
{
    "name": " CRM State History | CRM Status History | CRM Phase History | CRM Current State Log ",
    "author": "Creyox Technologies",
    "website": "https://www.creyox.com",
    "support": "support@creyox.com",
    "version": "15.0.0.1",
    "summary": """The CRM stage history is displayed with the help of this module. You can find out who they changed stages together with when. 
    We include a stage change analysis menu that lets you see a history of each step. 
    CRM State History
    CRM Status History
    CRM Phase History
    CRM Current State Log
    CRM Development Timeline
    CRM Milestone Tracker
    CRM State History in odoo
    CRM Status History in odoo
    CRM Phase History in odoo
    CRM Current State Log in odoo
    CRM Development Timeline in odoo
    CRM Milestone Tracker in odoo""",
    "sequence": 10,
    "description": """
    The stage history in the CRM is showcased through this module, allowing you to track who transitioned through stages and when. 
    We provide a stage change overview menu that enables you to view the history of each transition.
    CRM State History
    CRM Status History
    CRM Phase History
    CRM Current State Log
    CRM Development Timeline
    CRM Milestone Tracker
    CRM State History in odoo
    CRM Status History in odoo
    CRM Phase History in odoo
    CRM Current State Log in odoo
    CRM Development Timeline in odoo
    CRM Milestone Tracker in odoo
    """,
    "category": "Sales",
    "price": 0,
    "currency": "USD",
    "license": "OPL-1",
    "depends": ["base", "crm"],
    "data": [
        "security/ir.model.access.csv",
        "security/cr_crm_state_history_access_group.xml",
        "views/cr_crm_stage_change_history.xml",
        "views/crm_lead.xml",
        "views/cr_stage_change_analysis.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
    "images": ["static/description/banner.png"],
}
