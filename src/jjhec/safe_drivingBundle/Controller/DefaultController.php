<?php

namespace jjhec\safe_drivingBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;

class DefaultController extends Controller
{
    public function indexAction()
    {
        return $this->render('jjhecsafe_drivingBundle:Default:index.html.twig');
    }
}
