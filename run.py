from cmscore import AcehCMS


def application(environment, response):

    aceh = AcehCMS(environment)
    response(
        aceh.cms.resStatus,
        aceh.cms.resHeaders
    )
    return aceh.responseContent()
